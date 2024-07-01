import customtkinter as ctk
import serial
import serial.tools.list_ports
from GParser import parseGCode
import time
import threading

statesNum = 4
eventsNum = 6


states = {"WAITING_TRAJ":0, 
              "NOT_RUNNING":1, 
              "RUNNING": 2,
              "PAUSED": 3}

events = {"NO_EVENT":0,
              "TRAJ_LOADED":1,
              "START":2,
              "PAUSE":3,
              "RESUME":4,
              "STOP":5}

transitionMatrix = [[j for i in range(eventsNum)] for j in range(statesNum)]

transitionMatrix[states["WAITING_TRAJ"]][events["TRAJ_LOADED"]] = states["NOT_RUNNING"]
transitionMatrix[states["NOT_RUNNING"]][events["START"]] =  states["RUNNING"]
transitionMatrix[states["RUNNING"]][events["STOP"]] = states["NOT_RUNNING"]
transitionMatrix[states["RUNNING"]][events["PAUSE"]] = states["PAUSED"]
transitionMatrix[states["PAUSED"]][events["RESUME"]] = states["RUNNING"]
transitionMatrix[states["PAUSED"]][events["STOP"]] = states["NOT_RUNNING"]

buttonStates = [[] for _ in range(statesNum)]

buttonStates[states["WAITING_TRAJ"]]= [ctk.DISABLED, ctk.DISABLED, ctk.DISABLED, ctk.DISABLED, ctk.NORMAL]
buttonStates[states["RUNNING"]]= [ctk.DISABLED, ctk.NORMAL, ctk.DISABLED, ctk.NORMAL, ctk.DISABLED]
buttonStates[states["NOT_RUNNING"]]= [ctk.NORMAL, ctk.DISABLED, ctk.DISABLED, ctk.DISABLED, ctk.NORMAL]
buttonStates[states["PAUSED"]]= [ctk.DISABLED, ctk.DISABLED, ctk.NORMAL, ctk.NORMAL, ctk.DISABLED]

global state
global ser
state = states["WAITING_TRAJ"]
global blockFlag
blockFlag = False
global linhaAtual
linhaAtual = 0

def processResponse(response):
    global state
    global linhaAtual
    if(response == b':0115010177\r\n\r'):
        event = events["TRAJ_LOADED"]
        linhaAtual = 0
        linha_var.set("Linha atual: " + str(linhaAtual))
        textbox.tag_remove("highlight", "0.0", "end")
    elif(response == b':010602000116\r\n\r'):
        event = events["START"]
    elif(response == b':010602010115\r\n\r'):
        event = events["PAUSE"]
    elif(response == b':010602030113\r\n\r'):
        event =  events["RESUME"]
    elif(response == b':010602020114\r\n\r'):
        event =  events["STOP"]
        linhaAtual = 0
        linha_var.set("Linha atual: " + str(linhaAtual))
        textbox.tag_remove("highlight", "0.0", "end")
    elif(response[0:7] == b':010301'):
        linhaAtual = int(response[7:9].decode(),16)
        linha_var.set("Linha atual: " + str(linhaAtual+1))
        event = events["NO_EVENT"]
        for i in range(linhaAtual+2):
            textbox.tag_add("highlight",    f"{i}.0",f"{i}.end" )
    else:
        event =  events["NO_EVENT"]
    
    
    state = transitionMatrix[state][event]

    buttons =  buttonStates[state]

    start_button.configure(state=buttons[0])
    pause_button.configure(state=buttons[1])
    resume_button.configure(state=buttons[2])
    stop_button.configure(state=buttons[3])
    file_button.configure(state=buttons[4])

def calculate_lrc(data):
    lrc = 0
    for byte in data:
        lrc = (lrc + byte) & 0xFF  # Sum the bytes and keep only the least significant byte
    lrc -= 0x3A
    lrc = ((lrc ^ 0xFF) + 1) & 0xFF  # Two's complement

    lrc_string = hex(lrc)[2:]
    return lrc_string

def init_serial():
    global ser
    ports = list(serial.tools.list_ports.comports())
    com7_available = any(port.device == 'COM7' for port in ports)
    
    if com7_available:
        try:
            # Open the serial port with appropriate settings
            ser = serial.Serial(
                port='COM7',
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=0.5,
            )
        except serial.SerialException as e:
            print(f"Error: {e}")
    else:
        print("COM7 is not available")

def send_command(command):
    global ser
    global blockFlag

    
    blockFlag =  True
    ser.write(command)
    print("Sent to COM7 ->", command)
    
    # Optionally, read the response from the device (if needed)
    response = ser.read(16)  # Adjust the number of bytes to read as needed
    blockFlag =  False
    processResponse(response)
    if response:
        print("Received response:", response)
    
            
            
           

def send_trajectory():
    file, pointsNumber, trajectoryString = parseGCode()
    pointsNumber = "{:02X}".format(pointsNumber)
    global ser
    # Send the data
    message = b':0115' 
    message += pointsNumber.encode()  
    message += trajectoryString.encode()
    message += calculate_lrc(message).encode()
    message += b'\x0D\x0A'
    ser.write(message)
    print(message)
    
    # Optionally, read the response from the device (if needed)
    time.sleep(3)
    response = ser.read(100)  # Adjust the number of bytes to read as needed

    processResponse(response)

    if response:
        print("Received response:", response)
        textbox.delete("0.0", "end")  # delete all text
        lineNumber = 0
        for line in file:
            textbox.insert(f"{lineNumber}.0", line)
            lineNumber+=1
        textbox.tag_remove("highlight", "0.0", "end")

            
            
def request_currLine():
    # Send the data
    global ser
    global linhaAtual
    global blockFlag
   

    ser.write(b':0103000379' + b'\x0D\x0A' )
    
    
    # Optionally, read the response from the device (if needed)
    if(not blockFlag):
        response = ser.read(14)  # Adjust the number of bytes to read as needed
        processResponse(response)
        if response:
            print("Current line:", linhaAtual)
            
            
  

# Initialize the CustomTkinter application
app = ctk.CTk()
app.geometry("500x500")
app.title("COM7 Sender")



start_button = ctk.CTkButton(app, text="INICIAR", command=lambda:send_command(b':0106000178' + b'\x0D\x0A'))
start_button.grid(row=1, column=0, pady=10, padx=10)
pause_button = ctk.CTkButton(app, text="PAUSAR", command=lambda:send_command(b':0106010177' + b'\x0D\x0A'))
pause_button.grid(row=2, column=0, pady=10, padx=10)
resume_button = ctk.CTkButton(app, text="CONTINUAR", command=lambda:send_command(b':0106030175' + b'\x0D\x0A'))
resume_button.grid(row=3, column=0, pady=10, padx=10)
stop_button = ctk.CTkButton(app, text="PARAR", command=lambda:send_command(b':0106020176' + b'\x0D\x0A'))
stop_button.grid(row=4, column=0, pady=10, padx=10)
file_button = ctk.CTkButton(app, text="CARREGAR TRAJ.", command=send_trajectory)
file_button.grid(row=5, column=0, pady=10, padx=10)

buttons =  buttonStates[state]

start_button.configure(state=buttons[0])
pause_button.configure(state=buttons[1])
resume_button.configure(state=buttons[2])
stop_button.configure(state=buttons[3])
file_button.configure(state=buttons[4])

# Create a StringVar to hold the label text
linha_var = ctk.StringVar(value="Linha atual: " + str(linhaAtual))

# Create a label to display the global variable value
linha_label = ctk.CTkLabel(app, textvariable=linha_var)
linha_label.grid(row=0, column=1, rowspan=1, pady=10, padx=10)

textbox = ctk.CTkTextbox(app, width=300, height=400)
textbox.grid(row=1, column = 1,rowspan=7, pady=10, padx=10)


textbox.tag_config("highlight", background="#00ccff")


def background_loop():
    while True:
        if((state == states["RUNNING"]) & (not blockFlag)):
            request_currLine()
        time.sleep(0.1)

init_serial()

time.sleep(5)

background_thread = threading.Thread(target=background_loop, daemon=True)
background_thread.start()

# Run the application
app.mainloop()

ser.close()