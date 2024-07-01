# Generated from GCode.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,3,2,36,8,2,1,2,3,2,39,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,3,3,54,8,3,1,4,
        1,4,1,5,1,5,1,5,3,5,61,8,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,3,
        9,72,8,9,1,9,1,9,3,9,76,8,9,1,9,3,9,79,8,9,1,10,1,10,1,10,0,0,11,
        0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,5,6,1,0,10,12,81,0,23,1,0,0,
        0,2,29,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,55,1,0,0,0,10,60,1,0,
        0,0,12,62,1,0,0,0,14,64,1,0,0,0,16,67,1,0,0,0,18,71,1,0,0,0,20,80,
        1,0,0,0,22,24,3,4,2,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,27,1,0,0,0,27,28,3,2,1,0,28,1,1,0,0,0,29,30,3,6,
        3,0,30,31,3,8,4,0,31,3,1,0,0,0,32,33,3,6,3,0,33,35,3,12,6,0,34,36,
        3,14,7,0,35,34,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,39,3,16,8,
        0,38,37,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,3,20,10,0,41,48,
        1,0,0,0,42,43,3,6,3,0,43,44,3,10,5,0,44,45,3,20,10,0,45,48,1,0,0,
        0,46,48,3,20,10,0,47,32,1,0,0,0,47,42,1,0,0,0,47,46,1,0,0,0,48,5,
        1,0,0,0,49,50,5,1,0,0,50,51,5,13,0,0,51,53,5,13,0,0,52,54,5,13,0,
        0,53,52,1,0,0,0,53,54,1,0,0,0,54,7,1,0,0,0,55,56,5,2,0,0,56,9,1,
        0,0,0,57,61,5,3,0,0,58,59,5,4,0,0,59,61,5,16,0,0,60,57,1,0,0,0,60,
        58,1,0,0,0,61,11,1,0,0,0,62,63,7,0,0,0,63,13,1,0,0,0,64,65,5,7,0,
        0,65,66,3,18,9,0,66,15,1,0,0,0,67,68,5,8,0,0,68,69,3,18,9,0,69,17,
        1,0,0,0,70,72,5,9,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,
        73,75,5,13,0,0,74,76,5,13,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,79,5,13,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,19,1,0,0,0,
        80,81,7,1,0,0,81,21,1,0,0,0,9,25,35,38,47,53,60,71,75,78
    ]

class GCodeParser ( Parser ):

    grammarFileName = "GCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'N'", "'M30'", "'M02'", "'M01'", "'G01'", 
                     "'G00'", "'X'", "'Y'", "'-'", "'\\r'", "'\\n'", "'\\r\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "ID", "WS", "STRING" ]

    RULE_gcode = 0
    RULE_fimprograma = 1
    RULE_statement = 2
    RULE_numerolinha = 3
    RULE_mfim = 4
    RULE_mfunc = 5
    RULE_codfunc = 6
    RULE_coordx = 7
    RULE_coordy = 8
    RULE_coord = 9
    RULE_fimdelinha = 10

    ruleNames =  [ "gcode", "fimprograma", "statement", "numerolinha", "mfim", 
                   "mfunc", "codfunc", "coordx", "coordy", "coord", "fimdelinha" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INT=13
    ID=14
    WS=15
    STRING=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fimprograma(self):
            return self.getTypedRuleContext(GCodeParser.FimprogramaContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(GCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return GCodeParser.RULE_gcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGcode" ):
                listener.enterGcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGcode" ):
                listener.exitGcode(self)




    def gcode(self):

        localctx = GCodeParser.GcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 22
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 27
            self.fimprograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimprogramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(GCodeParser.NumerolinhaContext,0)


        def mfim(self):
            return self.getTypedRuleContext(GCodeParser.MfimContext,0)


        def getRuleIndex(self):
            return GCodeParser.RULE_fimprograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimprograma" ):
                listener.enterFimprograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimprograma" ):
                listener.exitFimprograma(self)




    def fimprograma(self):

        localctx = GCodeParser.FimprogramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fimprograma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.numerolinha()
            self.state = 30
            self.mfim()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(GCodeParser.NumerolinhaContext,0)


        def codfunc(self):
            return self.getTypedRuleContext(GCodeParser.CodfuncContext,0)


        def fimdelinha(self):
            return self.getTypedRuleContext(GCodeParser.FimdelinhaContext,0)


        def coordx(self):
            return self.getTypedRuleContext(GCodeParser.CoordxContext,0)


        def coordy(self):
            return self.getTypedRuleContext(GCodeParser.CoordyContext,0)


        def mfunc(self):
            return self.getTypedRuleContext(GCodeParser.MfuncContext,0)


        def getRuleIndex(self):
            return GCodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.numerolinha()
                self.state = 33
                self.codfunc()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 34
                    self.coordx()


                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 37
                    self.coordy()


                self.state = 40
                self.fimdelinha()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.numerolinha()
                self.state = 43
                self.mfunc()
                self.state = 44
                self.fimdelinha()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.fimdelinha()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerolinhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GCodeParser.INT)
            else:
                return self.getToken(GCodeParser.INT, i)

        def getRuleIndex(self):
            return GCodeParser.RULE_numerolinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumerolinha" ):
                listener.enterNumerolinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumerolinha" ):
                listener.exitNumerolinha(self)




    def numerolinha(self):

        localctx = GCodeParser.NumerolinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numerolinha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GCodeParser.T__0)
            self.state = 50
            self.match(GCodeParser.INT)
            self.state = 51
            self.match(GCodeParser.INT)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 52
                self.match(GCodeParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GCodeParser.RULE_mfim

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfim" ):
                listener.enterMfim(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfim" ):
                listener.exitMfim(self)




    def mfim(self):

        localctx = GCodeParser.MfimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mfim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GCodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GCodeParser.STRING, 0)

        def getRuleIndex(self):
            return GCodeParser.RULE_mfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfunc" ):
                listener.enterMfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfunc" ):
                listener.exitMfunc(self)




    def mfunc(self):

        localctx = GCodeParser.MfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mfunc)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(GCodeParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(GCodeParser.T__3)
                self.state = 59
                self.match(GCodeParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GCodeParser.RULE_codfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodfunc" ):
                listener.enterCodfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodfunc" ):
                listener.exitCodfunc(self)




    def codfunc(self):

        localctx = GCodeParser.CodfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_codfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(GCodeParser.CoordContext,0)


        def getRuleIndex(self):
            return GCodeParser.RULE_coordx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordx" ):
                listener.enterCoordx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordx" ):
                listener.exitCoordx(self)




    def coordx(self):

        localctx = GCodeParser.CoordxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_coordx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GCodeParser.T__6)
            self.state = 65
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coord(self):
            return self.getTypedRuleContext(GCodeParser.CoordContext,0)


        def getRuleIndex(self):
            return GCodeParser.RULE_coordy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordy" ):
                listener.enterCoordy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordy" ):
                listener.exitCoordy(self)




    def coordy(self):

        localctx = GCodeParser.CoordyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(GCodeParser.T__7)
            self.state = 68
            self.coord()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GCodeParser.INT)
            else:
                return self.getToken(GCodeParser.INT, i)

        def getRuleIndex(self):
            return GCodeParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)




    def coord(self):

        localctx = GCodeParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_coord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 70
                self.match(GCodeParser.T__8)


            self.state = 73
            self.match(GCodeParser.INT)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(GCodeParser.INT)


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 77
                self.match(GCodeParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimdelinhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GCodeParser.RULE_fimdelinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimdelinha" ):
                listener.enterFimdelinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimdelinha" ):
                listener.exitFimdelinha(self)




    def fimdelinha(self):

        localctx = GCodeParser.FimdelinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fimdelinha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





