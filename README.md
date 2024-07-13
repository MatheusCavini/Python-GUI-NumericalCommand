# Python GUI for Numerical Commands
## Introduction
This projects implements a Graphic User Interface built with Python CustomTKinter, put together with a simple G Code Parser, for sending a trajectory file and execution commands to a prototype robotic leg.

It was built as part of the Integrated Project of 7th Semester (PI7) for my Mechatronics Engineering course at Escola Politécnica da Universide de São Paulo (USP).

Communication between the interface and the hardware of the leg is done by MODBUS commands via serial.

## Demonstration

![GUI](https://github.com/user-attachments/assets/072060f3-bf97-4130-ac64-882f36b97c84)

## Features
• Loading and sending a trajectory from a local G Code.<br/>
• Setting Proportional, Integrative and Derivative control constants for both hip and knee joints.<br/>
• Sending commands to control the execution of the trajectory: Go to origin, Start, Stop, Pause and Resume.<br/>
• Display in real time the line number currently executing as well as highlighting it on G Code.<br/>
  
