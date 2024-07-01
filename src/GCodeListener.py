# Generated from GCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GCodeParser import GCodeParser
else:
    from GCodeParser import GCodeParser

# This class defines a complete listener for a parse tree produced by GCodeParser.
class GCodeListener(ParseTreeListener):

    # Enter a parse tree produced by GCodeParser#gcode.
    def enterGcode(self, ctx:GCodeParser.GcodeContext):
        pass

    # Exit a parse tree produced by GCodeParser#gcode.
    def exitGcode(self, ctx:GCodeParser.GcodeContext):
        pass


    # Enter a parse tree produced by GCodeParser#fimprograma.
    def enterFimprograma(self, ctx:GCodeParser.FimprogramaContext):
        pass

    # Exit a parse tree produced by GCodeParser#fimprograma.
    def exitFimprograma(self, ctx:GCodeParser.FimprogramaContext):
        pass


    # Enter a parse tree produced by GCodeParser#statement.
    def enterStatement(self, ctx:GCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by GCodeParser#statement.
    def exitStatement(self, ctx:GCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by GCodeParser#numerolinha.
    def enterNumerolinha(self, ctx:GCodeParser.NumerolinhaContext):
        pass

    # Exit a parse tree produced by GCodeParser#numerolinha.
    def exitNumerolinha(self, ctx:GCodeParser.NumerolinhaContext):
        pass


    # Enter a parse tree produced by GCodeParser#mfim.
    def enterMfim(self, ctx:GCodeParser.MfimContext):
        pass

    # Exit a parse tree produced by GCodeParser#mfim.
    def exitMfim(self, ctx:GCodeParser.MfimContext):
        pass


    # Enter a parse tree produced by GCodeParser#mfunc.
    def enterMfunc(self, ctx:GCodeParser.MfuncContext):
        pass

    # Exit a parse tree produced by GCodeParser#mfunc.
    def exitMfunc(self, ctx:GCodeParser.MfuncContext):
        pass


    # Enter a parse tree produced by GCodeParser#codfunc.
    def enterCodfunc(self, ctx:GCodeParser.CodfuncContext):
        pass

    # Exit a parse tree produced by GCodeParser#codfunc.
    def exitCodfunc(self, ctx:GCodeParser.CodfuncContext):
        pass


    # Enter a parse tree produced by GCodeParser#coordx.
    def enterCoordx(self, ctx:GCodeParser.CoordxContext):
        pass

    # Exit a parse tree produced by GCodeParser#coordx.
    def exitCoordx(self, ctx:GCodeParser.CoordxContext):
        pass


    # Enter a parse tree produced by GCodeParser#coordy.
    def enterCoordy(self, ctx:GCodeParser.CoordyContext):
        pass

    # Exit a parse tree produced by GCodeParser#coordy.
    def exitCoordy(self, ctx:GCodeParser.CoordyContext):
        pass


    # Enter a parse tree produced by GCodeParser#coord.
    def enterCoord(self, ctx:GCodeParser.CoordContext):
        pass

    # Exit a parse tree produced by GCodeParser#coord.
    def exitCoord(self, ctx:GCodeParser.CoordContext):
        pass


    # Enter a parse tree produced by GCodeParser#fimdelinha.
    def enterFimdelinha(self, ctx:GCodeParser.FimdelinhaContext):
        pass

    # Exit a parse tree produced by GCodeParser#fimdelinha.
    def exitFimdelinha(self, ctx:GCodeParser.FimdelinhaContext):
        pass



del GCodeParser