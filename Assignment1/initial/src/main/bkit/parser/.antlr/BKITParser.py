# Generated from d:\HK201\PPL\Assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Do'", 
                     "'EndDo'", "'Continue'", "'If'", "'ElseIf'", "'Else'", 
                     "'EndBody'", "'EndIf'", "'For'", "'EndFor'", "'While'", 
                     "'EndWhile'", "'Function'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'True'", "'False'", "'-'", "'+'", 
                     "'*'", "'\\'", "'%'", "'-.'", "'+.'", "'*.'", "'\\.'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "BREAK", "DO", "ENDDO", 
                      "CONTINUE", "IF", "ELSEIF", "ELSE", "ENDBODY", "ENDIF", 
                      "FOR", "ENDFOR", "WHILE", "ENDWHILE", "FUNCTION", 
                      "PARAMETER", "RETURN", "THEN", "VAR", "TRUE", "FALSE", 
                      "SUB", "ADD", "MUL", "DIV", "RM", "SUBFLT", "ADDFLT", 
                      "MULFLT", "DIVFLT", "NEG", "CONJ", "DISJ", "EQ", "NEQ", 
                      "LES", "GRE", "LESEQ", "GREEQ", "NEQFLT", "LESSFLT", 
                      "GREFLT", "LESEQFLT", "GREEQFLT", "LP", "RP", "LSB", 
                      "RSB", "LCB", "RCB", "SEMI", "COLON", "COMMA", "DOT", 
                      "INTERGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    BREAK=3
    DO=4
    ENDDO=5
    CONTINUE=6
    IF=7
    ELSEIF=8
    ELSE=9
    ENDBODY=10
    ENDIF=11
    FOR=12
    ENDFOR=13
    WHILE=14
    ENDWHILE=15
    FUNCTION=16
    PARAMETER=17
    RETURN=18
    THEN=19
    VAR=20
    TRUE=21
    FALSE=22
    SUB=23
    ADD=24
    MUL=25
    DIV=26
    RM=27
    SUBFLT=28
    ADDFLT=29
    MULFLT=30
    DIVFLT=31
    NEG=32
    CONJ=33
    DISJ=34
    EQ=35
    NEQ=36
    LES=37
    GRE=38
    LESEQ=39
    GREEQ=40
    NEQFLT=41
    LESSFLT=42
    GREFLT=43
    LESEQFLT=44
    GREEQFLT=45
    LP=46
    RP=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    SEMI=52
    COLON=53
    COMMA=54
    DOT=55
    INTERGER_LITERAL=56
    FLOAT_LITERAL=57
    BOOLEAN_LITERAL=58
    STRING_LITERAL=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





