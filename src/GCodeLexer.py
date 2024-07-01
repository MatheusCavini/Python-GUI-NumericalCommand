# Generated from GCode.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,88,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        4,14,74,8,14,11,14,12,14,75,1,14,1,14,1,15,1,15,5,15,82,8,15,10,
        15,12,15,85,9,15,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,1,0,2,3,0,9,
        10,13,13,32,32,2,0,34,34,92,92,89,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,
        0,0,5,39,1,0,0,0,7,43,1,0,0,0,9,47,1,0,0,0,11,51,1,0,0,0,13,55,1,
        0,0,0,15,57,1,0,0,0,17,59,1,0,0,0,19,61,1,0,0,0,21,63,1,0,0,0,23,
        65,1,0,0,0,25,68,1,0,0,0,27,70,1,0,0,0,29,73,1,0,0,0,31,79,1,0,0,
        0,33,34,5,78,0,0,34,2,1,0,0,0,35,36,5,77,0,0,36,37,5,51,0,0,37,38,
        5,48,0,0,38,4,1,0,0,0,39,40,5,77,0,0,40,41,5,48,0,0,41,42,5,50,0,
        0,42,6,1,0,0,0,43,44,5,77,0,0,44,45,5,48,0,0,45,46,5,49,0,0,46,8,
        1,0,0,0,47,48,5,71,0,0,48,49,5,48,0,0,49,50,5,49,0,0,50,10,1,0,0,
        0,51,52,5,71,0,0,52,53,5,48,0,0,53,54,5,48,0,0,54,12,1,0,0,0,55,
        56,5,88,0,0,56,14,1,0,0,0,57,58,5,89,0,0,58,16,1,0,0,0,59,60,5,45,
        0,0,60,18,1,0,0,0,61,62,5,13,0,0,62,20,1,0,0,0,63,64,5,10,0,0,64,
        22,1,0,0,0,65,66,5,13,0,0,66,67,5,10,0,0,67,24,1,0,0,0,68,69,2,48,
        57,0,69,26,1,0,0,0,70,71,2,97,122,0,71,28,1,0,0,0,72,74,7,0,0,0,
        73,72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,77,1,
        0,0,0,77,78,6,14,0,0,78,30,1,0,0,0,79,83,5,34,0,0,80,82,8,1,0,0,
        81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,
        0,0,0,85,83,1,0,0,0,86,87,5,34,0,0,87,32,1,0,0,0,3,0,75,83,1,6,0,
        0
    ]

class GCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    INT = 13
    ID = 14
    WS = 15
    STRING = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'N'", "'M30'", "'M02'", "'M01'", "'G01'", "'G00'", "'X'", "'Y'", 
            "'-'", "'\\r'", "'\\n'", "'\\r\\n'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS", "STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "INT", "ID", 
                  "WS", "STRING" ]

    grammarFileName = "GCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


