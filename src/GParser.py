from antlr4 import *
from GCodeLexer import GCodeLexer
from GCodeParser import GCodeParser
from GCodeListener import GCodeListener



class WalkListener(GCodeListener):
    def __init__(self):
        self.trajectoryFile = ""
        self.pointsNumber = 0

    def enterStatement(self, ctx):
        if ctx.codfunc() is not None:
            #print(ctx.codfunc().getText())
            pass 
        if ctx.coordx() is not None:
            #print(ctx.coordx().coord().getText())
            self.trajectoryFile += "{:04.1f}".format(int(ctx.coordx().coord().getText())/10)
        else:
            self.trajectoryFile += "00.0"
        if ctx.coordy() is not None:
            #print(ctx.coordy().coord().getText())
            self.trajectoryFile += "{:04.1f}".format(int(ctx.coordy().coord().getText())/10)
        else:
            self.trajectoryFile += "00.0"


        self.trajectoryFile += "00.0" #coordenada Z = 00.0
        self.pointsNumber += 1


def parseGCode():
    with open("./src/GCode-example") as file:
        data = f'{file.read()}'
    lexer = GCodeLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = GCodeParser(stream)
    tree = parser.gcode()
    #print(tree.toStringTree(recog=parser))
    listener = WalkListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return (data, listener.pointsNumber, listener.trajectoryFile)


