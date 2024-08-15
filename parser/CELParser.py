# Generated from grammar/CEL.g4 by ANTLR 4.13.0
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
        4,1,36,209,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,5,2,41,8,2,10,
        2,12,2,44,9,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,6,1,6,4,6,81,8,6,11,
        6,12,6,82,1,6,1,6,4,6,87,8,6,11,6,12,6,88,1,6,3,6,92,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,102,8,7,1,7,3,7,105,8,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,3,7,115,8,7,1,7,3,7,118,8,7,1,7,5,7,121,8,7,
        10,7,12,7,124,9,7,1,8,3,8,127,8,8,1,8,1,8,1,8,3,8,132,8,8,1,8,3,
        8,135,8,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,143,8,8,1,8,3,8,146,8,8,1,
        8,1,8,1,8,3,8,151,8,8,1,8,3,8,154,8,8,1,8,1,8,3,8,158,8,8,1,9,1,
        9,1,9,5,9,163,8,9,10,9,12,9,166,9,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,175,8,10,10,10,12,10,178,9,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,188,8,11,10,11,12,11,191,9,11,1,12,3,12,194,
        8,12,1,12,1,12,1,12,3,12,199,8,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,207,8,12,1,12,0,3,8,10,14,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,3,1,0,1,7,1,0,23,25,2,0,18,18,22,22,235,0,26,1,0,0,0,2,29,1,
        0,0,0,4,37,1,0,0,0,6,45,1,0,0,0,8,53,1,0,0,0,10,64,1,0,0,0,12,91,
        1,0,0,0,14,93,1,0,0,0,16,157,1,0,0,0,18,159,1,0,0,0,20,167,1,0,0,
        0,22,179,1,0,0,0,24,206,1,0,0,0,26,27,3,2,1,0,27,28,5,0,0,1,28,1,
        1,0,0,0,29,35,3,4,2,0,30,31,5,20,0,0,31,32,3,4,2,0,32,33,5,21,0,
        0,33,34,3,2,1,0,34,36,1,0,0,0,35,30,1,0,0,0,35,36,1,0,0,0,36,3,1,
        0,0,0,37,42,3,6,3,0,38,39,5,9,0,0,39,41,3,6,3,0,40,38,1,0,0,0,41,
        44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,42,1,0,0,
        0,45,50,3,8,4,0,46,47,5,8,0,0,47,49,3,8,4,0,48,46,1,0,0,0,49,52,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,
        54,6,4,-1,0,54,55,3,10,5,0,55,61,1,0,0,0,56,57,10,1,0,0,57,58,7,
        0,0,0,58,60,3,8,4,2,59,56,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,
        62,1,0,0,0,62,9,1,0,0,0,63,61,1,0,0,0,64,65,6,5,-1,0,65,66,3,12,
        6,0,66,75,1,0,0,0,67,68,10,2,0,0,68,69,7,1,0,0,69,74,3,10,5,3,70,
        71,10,1,0,0,71,72,7,2,0,0,72,74,3,10,5,2,73,67,1,0,0,0,73,70,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,11,1,0,0,0,77,75,
        1,0,0,0,78,92,3,14,7,0,79,81,5,19,0,0,80,79,1,0,0,0,81,82,1,0,0,
        0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,92,3,14,7,0,85,87,
        5,18,0,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,90,1,0,0,0,90,92,3,14,7,0,91,78,1,0,0,0,91,80,1,0,0,0,91,86,1,
        0,0,0,92,13,1,0,0,0,93,94,6,7,-1,0,94,95,3,16,8,0,95,122,1,0,0,0,
        96,97,10,3,0,0,97,98,5,16,0,0,98,104,5,36,0,0,99,101,5,14,0,0,100,
        102,3,18,9,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,
        105,5,15,0,0,104,99,1,0,0,0,104,105,1,0,0,0,105,121,1,0,0,0,106,
        107,10,2,0,0,107,108,5,10,0,0,108,109,3,2,1,0,109,110,5,11,0,0,110,
        121,1,0,0,0,111,112,10,1,0,0,112,114,5,12,0,0,113,115,3,20,10,0,
        114,113,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,5,17,0,0,
        117,116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,121,5,13,0,0,
        120,96,1,0,0,0,120,106,1,0,0,0,120,111,1,0,0,0,121,124,1,0,0,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,15,1,0,0,0,124,122,1,0,0,0,125,127,
        5,16,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,134,
        5,36,0,0,129,131,5,14,0,0,130,132,3,18,9,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,133,1,0,0,0,133,135,5,15,0,0,134,129,1,0,0,0,134,135,
        1,0,0,0,135,158,1,0,0,0,136,137,5,14,0,0,137,138,3,2,1,0,138,139,
        5,15,0,0,139,158,1,0,0,0,140,142,5,10,0,0,141,143,3,18,9,0,142,141,
        1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,146,5,17,0,0,145,144,
        1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,158,5,11,0,0,148,150,
        5,12,0,0,149,151,3,22,11,0,150,149,1,0,0,0,150,151,1,0,0,0,151,153,
        1,0,0,0,152,154,5,17,0,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,
        1,0,0,0,155,158,5,13,0,0,156,158,3,24,12,0,157,126,1,0,0,0,157,136,
        1,0,0,0,157,140,1,0,0,0,157,148,1,0,0,0,157,156,1,0,0,0,158,17,1,
        0,0,0,159,164,3,2,1,0,160,161,5,17,0,0,161,163,3,2,1,0,162,160,1,
        0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,19,1,0,
        0,0,166,164,1,0,0,0,167,168,5,36,0,0,168,169,5,21,0,0,169,176,3,
        2,1,0,170,171,5,17,0,0,171,172,5,36,0,0,172,173,5,21,0,0,173,175,
        3,2,1,0,174,170,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,21,1,0,0,0,178,176,1,0,0,0,179,180,3,2,1,0,180,181,5,
        21,0,0,181,189,3,2,1,0,182,183,5,17,0,0,183,184,3,2,1,0,184,185,
        5,21,0,0,185,186,3,2,1,0,186,188,1,0,0,0,187,182,1,0,0,0,188,191,
        1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,23,1,0,0,0,191,189,1,
        0,0,0,192,194,5,18,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,1,
        0,0,0,195,207,5,32,0,0,196,207,5,33,0,0,197,199,5,18,0,0,198,197,
        1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,200,207,5,31,0,0,201,207,
        5,34,0,0,202,207,5,35,0,0,203,207,5,26,0,0,204,207,5,27,0,0,205,
        207,5,28,0,0,206,193,1,0,0,0,206,196,1,0,0,0,206,198,1,0,0,0,206,
        201,1,0,0,0,206,202,1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,0,206,
        205,1,0,0,0,207,25,1,0,0,0,29,35,42,50,61,73,75,82,88,91,101,104,
        114,117,120,122,126,131,134,142,145,150,153,157,164,176,189,193,
        198,206
    ]

class CELParser ( Parser ):

    grammarFileName = "CEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'in'", "'<'", "'<='", 
                     "'>='", "'>'", "'&&'", "'||'", "'['", "']'", "'{'", 
                     "'}'", "'('", "')'", "'.'", "','", "'-'", "'!'", "'?'", 
                     "':'", "'+'", "'*'", "'/'", "'%'", "'true'", "'false'", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "EQUALS", "NOT_EQUALS", "IN", "LESS", 
                      "LESS_EQUALS", "GREATER_EQUALS", "GREATER", "LOGICAL_AND", 
                      "LOGICAL_OR", "LBRACKET", "RPRACKET", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "DOT", "COMMA", "MINUS", "EXCLAM", 
                      "QUESTIONMARK", "COLON", "PLUS", "STAR", "SLASH", 
                      "PERCENT", "TRUE", "FALSE", "NULL", "WHITESPACE", 
                      "COMMENT", "NUM_FLOAT", "NUM_INT", "NUM_UINT", "STRING", 
                      "BYTES", "IDENTIFIER" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_conditionalOr = 2
    RULE_conditionalAnd = 3
    RULE_relation = 4
    RULE_calc = 5
    RULE_unary = 6
    RULE_member = 7
    RULE_primary = 8
    RULE_exprList = 9
    RULE_fieldInitializerList = 10
    RULE_mapInitializerList = 11
    RULE_literal = 12

    ruleNames =  [ "start", "expr", "conditionalOr", "conditionalAnd", "relation", 
                   "calc", "unary", "member", "primary", "exprList", "fieldInitializerList", 
                   "mapInitializerList", "literal" ]

    EOF = Token.EOF
    EQUALS=1
    NOT_EQUALS=2
    IN=3
    LESS=4
    LESS_EQUALS=5
    GREATER_EQUALS=6
    GREATER=7
    LOGICAL_AND=8
    LOGICAL_OR=9
    LBRACKET=10
    RPRACKET=11
    LBRACE=12
    RBRACE=13
    LPAREN=14
    RPAREN=15
    DOT=16
    COMMA=17
    MINUS=18
    EXCLAM=19
    QUESTIONMARK=20
    COLON=21
    PLUS=22
    STAR=23
    SLASH=24
    PERCENT=25
    TRUE=26
    FALSE=27
    NULL=28
    WHITESPACE=29
    COMMENT=30
    NUM_FLOAT=31
    NUM_INT=32
    NUM_UINT=33
    STRING=34
    BYTES=35
    IDENTIFIER=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # ExprContext

        def EOF(self):
            return self.getToken(CELParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(CELParser.ExprContext,0)


        def getRuleIndex(self):
            return CELParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = CELParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            localctx.e = self.expr()
            self.state = 27
            self.match(CELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # ConditionalOrContext
            self.op = None # Token
            self.e1 = None # ConditionalOrContext
            self.e2 = None # ExprContext

        def conditionalOr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.ConditionalOrContext)
            else:
                return self.getTypedRuleContext(CELParser.ConditionalOrContext,i)


        def COLON(self):
            return self.getToken(CELParser.COLON, 0)

        def QUESTIONMARK(self):
            return self.getToken(CELParser.QUESTIONMARK, 0)

        def expr(self):
            return self.getTypedRuleContext(CELParser.ExprContext,0)


        def getRuleIndex(self):
            return CELParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CELParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            localctx.e = self.conditionalOr()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 30
                localctx.op = self.match(CELParser.QUESTIONMARK)
                self.state = 31
                localctx.e1 = self.conditionalOr()
                self.state = 32
                self.match(CELParser.COLON)
                self.state = 33
                localctx.e2 = self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # ConditionalAndContext
            self.s9 = None # Token
            self.ops = list() # of Tokens
            self._conditionalAnd = None # ConditionalAndContext
            self.e1 = list() # of ConditionalAndContexts

        def conditionalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.ConditionalAndContext)
            else:
                return self.getTypedRuleContext(CELParser.ConditionalAndContext,i)


        def LOGICAL_OR(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.LOGICAL_OR)
            else:
                return self.getToken(CELParser.LOGICAL_OR, i)

        def getRuleIndex(self):
            return CELParser.RULE_conditionalOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOr" ):
                listener.enterConditionalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOr" ):
                listener.exitConditionalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalOr" ):
                return visitor.visitConditionalOr(self)
            else:
                return visitor.visitChildren(self)




    def conditionalOr(self):

        localctx = CELParser.ConditionalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.e = self.conditionalAnd()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 38
                localctx.s9 = self.match(CELParser.LOGICAL_OR)
                localctx.ops.append(localctx.s9)
                self.state = 39
                localctx._conditionalAnd = self.conditionalAnd()
                localctx.e1.append(localctx._conditionalAnd)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # RelationContext
            self.s8 = None # Token
            self.ops = list() # of Tokens
            self._relation = None # RelationContext
            self.e1 = list() # of RelationContexts

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.RelationContext)
            else:
                return self.getTypedRuleContext(CELParser.RelationContext,i)


        def LOGICAL_AND(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.LOGICAL_AND)
            else:
                return self.getToken(CELParser.LOGICAL_AND, i)

        def getRuleIndex(self):
            return CELParser.RULE_conditionalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalAnd" ):
                listener.enterConditionalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalAnd" ):
                listener.exitConditionalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalAnd" ):
                return visitor.visitConditionalAnd(self)
            else:
                return visitor.visitChildren(self)




    def conditionalAnd(self):

        localctx = CELParser.ConditionalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditionalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            localctx.e = self.relation(0)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 46
                localctx.s8 = self.match(CELParser.LOGICAL_AND)
                localctx.ops.append(localctx.s8)
                self.state = 47
                localctx._relation = self.relation(0)
                localctx.e1.append(localctx._relation)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_relation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RelationOpContext(RelationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.RelationContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.RelationContext)
            else:
                return self.getTypedRuleContext(CELParser.RelationContext,i)

        def LESS(self):
            return self.getToken(CELParser.LESS, 0)
        def LESS_EQUALS(self):
            return self.getToken(CELParser.LESS_EQUALS, 0)
        def GREATER_EQUALS(self):
            return self.getToken(CELParser.GREATER_EQUALS, 0)
        def GREATER(self):
            return self.getToken(CELParser.GREATER, 0)
        def EQUALS(self):
            return self.getToken(CELParser.EQUALS, 0)
        def NOT_EQUALS(self):
            return self.getToken(CELParser.NOT_EQUALS, 0)
        def IN(self):
            return self.getToken(CELParser.IN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationOp" ):
                listener.enterRelationOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationOp" ):
                listener.exitRelationOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationOp" ):
                return visitor.visitRelationOp(self)
            else:
                return visitor.visitChildren(self)


    class RelationCalcContext(RelationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.RelationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def calc(self):
            return self.getTypedRuleContext(CELParser.CalcContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationCalc" ):
                listener.enterRelationCalc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationCalc" ):
                listener.exitRelationCalc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationCalc" ):
                return visitor.visitRelationCalc(self)
            else:
                return visitor.visitChildren(self)



    def relation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CELParser.RelationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_relation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CELParser.RelationCalcContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 54
            self.calc(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CELParser.RelationOpContext(self, CELParser.RelationContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 56
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 57
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 58
                    self.relation(2) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CalcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_calc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CalcMulDivContext(CalcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.CalcContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def calc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.CalcContext)
            else:
                return self.getTypedRuleContext(CELParser.CalcContext,i)

        def STAR(self):
            return self.getToken(CELParser.STAR, 0)
        def SLASH(self):
            return self.getToken(CELParser.SLASH, 0)
        def PERCENT(self):
            return self.getToken(CELParser.PERCENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalcMulDiv" ):
                listener.enterCalcMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalcMulDiv" ):
                listener.exitCalcMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalcMulDiv" ):
                return visitor.visitCalcMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class CalcUnaryContext(CalcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.CalcContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(CELParser.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalcUnary" ):
                listener.enterCalcUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalcUnary" ):
                listener.exitCalcUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalcUnary" ):
                return visitor.visitCalcUnary(self)
            else:
                return visitor.visitChildren(self)


    class CalcAddSubContext(CalcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.CalcContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def calc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.CalcContext)
            else:
                return self.getTypedRuleContext(CELParser.CalcContext,i)

        def PLUS(self):
            return self.getToken(CELParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CELParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalcAddSub" ):
                listener.enterCalcAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalcAddSub" ):
                listener.exitCalcAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalcAddSub" ):
                return visitor.visitCalcAddSub(self)
            else:
                return visitor.visitChildren(self)



    def calc(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CELParser.CalcContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_calc, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CELParser.CalcUnaryContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 65
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CELParser.CalcMulDivContext(self, CELParser.CalcContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calc)
                        self.state = 67
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 68
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.calc(3)
                        pass

                    elif la_ == 2:
                        localctx = CELParser.CalcAddSubContext(self, CELParser.CalcContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calc)
                        self.state = 70
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 71
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.calc(2)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicalNotContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.UnaryContext
            super().__init__(parser)
            self.s19 = None # Token
            self.ops = list() # of Tokens
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)

        def EXCLAM(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.EXCLAM)
            else:
                return self.getToken(CELParser.EXCLAM, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class MemberExprContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberExpr" ):
                listener.enterMemberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberExpr" ):
                listener.exitMemberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberExpr" ):
                return visitor.visitMemberExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegateContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.UnaryContext
            super().__init__(parser)
            self.s18 = None # Token
            self.ops = list() # of Tokens
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.MINUS)
            else:
                return self.getToken(CELParser.MINUS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegate" ):
                listener.enterNegate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegate" ):
                listener.exitNegate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate" ):
                return visitor.visitNegate(self)
            else:
                return visitor.visitChildren(self)



    def unary(self):

        localctx = CELParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = CELParser.MemberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.member(0)
                pass

            elif la_ == 2:
                localctx = CELParser.LogicalNotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    localctx.s19 = self.match(CELParser.EXCLAM)
                    localctx.ops.append(localctx.s19)
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==19):
                        break

                self.state = 84
                self.member(0)
                pass

            elif la_ == 3:
                localctx = CELParser.NegateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 86 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 85
                        localctx.s18 = self.match(CELParser.MINUS)
                        localctx.ops.append(localctx.s18)

                    else:
                        raise NoViableAltException(self)
                    self.state = 88 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 90
                self.member(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_member

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SelectOrCallContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.MemberContext
            super().__init__(parser)
            self.op = None # Token
            self.id_ = None # Token
            self.open_ = None # Token
            self.args = None # ExprListContext
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)

        def DOT(self):
            return self.getToken(CELParser.DOT, 0)
        def IDENTIFIER(self):
            return self.getToken(CELParser.IDENTIFIER, 0)
        def RPAREN(self):
            return self.getToken(CELParser.RPAREN, 0)
        def LPAREN(self):
            return self.getToken(CELParser.LPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(CELParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectOrCall" ):
                listener.enterSelectOrCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectOrCall" ):
                listener.exitSelectOrCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectOrCall" ):
                return visitor.visitSelectOrCall(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExprContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.MemberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(CELParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class IndexContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.MemberContext
            super().__init__(parser)
            self.op = None # Token
            self.index = None # ExprContext
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)

        def RPRACKET(self):
            return self.getToken(CELParser.RPRACKET, 0)
        def LBRACKET(self):
            return self.getToken(CELParser.LBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(CELParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)


    class CreateMessageContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.MemberContext
            super().__init__(parser)
            self.op = None # Token
            self.entries = None # FieldInitializerListContext
            self.copyFrom(ctx)

        def member(self):
            return self.getTypedRuleContext(CELParser.MemberContext,0)

        def RBRACE(self):
            return self.getToken(CELParser.RBRACE, 0)
        def LBRACE(self):
            return self.getToken(CELParser.LBRACE, 0)
        def COMMA(self):
            return self.getToken(CELParser.COMMA, 0)
        def fieldInitializerList(self):
            return self.getTypedRuleContext(CELParser.FieldInitializerListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateMessage" ):
                listener.enterCreateMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateMessage" ):
                listener.exitCreateMessage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateMessage" ):
                return visitor.visitCreateMessage(self)
            else:
                return visitor.visitChildren(self)



    def member(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CELParser.MemberContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_member, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CELParser.PrimaryExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 94
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = CELParser.SelectOrCallContext(self, CELParser.MemberContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member)
                        self.state = 96
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 97
                        localctx.op = self.match(CELParser.DOT)
                        self.state = 98
                        localctx.id_ = self.match(CELParser.IDENTIFIER)
                        self.state = 104
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                        if la_ == 1:
                            self.state = 99
                            localctx.open_ = self.match(CELParser.LPAREN)
                            self.state = 101
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135762105344) != 0):
                                self.state = 100
                                localctx.args = self.exprList()


                            self.state = 103
                            self.match(CELParser.RPAREN)


                        pass

                    elif la_ == 2:
                        localctx = CELParser.IndexContext(self, CELParser.MemberContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member)
                        self.state = 106
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 107
                        localctx.op = self.match(CELParser.LBRACKET)
                        self.state = 108
                        localctx.index = self.expr()
                        self.state = 109
                        self.match(CELParser.RPRACKET)
                        pass

                    elif la_ == 3:
                        localctx = CELParser.CreateMessageContext(self, CELParser.MemberContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member)
                        self.state = 111
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 112
                        localctx.op = self.match(CELParser.LBRACE)
                        self.state = 114
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==36:
                            self.state = 113
                            localctx.entries = self.fieldInitializerList()


                        self.state = 117
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==17:
                            self.state = 116
                            self.match(CELParser.COMMA)


                        self.state = 119
                        self.match(CELParser.RBRACE)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CreateListContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.PrimaryContext
            super().__init__(parser)
            self.op = None # Token
            self.elems = None # ExprListContext
            self.copyFrom(ctx)

        def RPRACKET(self):
            return self.getToken(CELParser.RPRACKET, 0)
        def LBRACKET(self):
            return self.getToken(CELParser.LBRACKET, 0)
        def COMMA(self):
            return self.getToken(CELParser.COMMA, 0)
        def exprList(self):
            return self.getTypedRuleContext(CELParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateList" ):
                listener.enterCreateList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateList" ):
                listener.exitCreateList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateList" ):
                return visitor.visitCreateList(self)
            else:
                return visitor.visitChildren(self)


    class CreateStructContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.PrimaryContext
            super().__init__(parser)
            self.op = None # Token
            self.entries = None # MapInitializerListContext
            self.copyFrom(ctx)

        def RBRACE(self):
            return self.getToken(CELParser.RBRACE, 0)
        def LBRACE(self):
            return self.getToken(CELParser.LBRACE, 0)
        def COMMA(self):
            return self.getToken(CELParser.COMMA, 0)
        def mapInitializerList(self):
            return self.getTypedRuleContext(CELParser.MapInitializerListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStruct" ):
                listener.enterCreateStruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStruct" ):
                listener.exitCreateStruct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStruct" ):
                return visitor.visitCreateStruct(self)
            else:
                return visitor.visitChildren(self)


    class ConstantLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(CELParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantLiteral" ):
                listener.enterConstantLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantLiteral" ):
                listener.exitConstantLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantLiteral" ):
                return visitor.visitConstantLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NestedContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.PrimaryContext
            super().__init__(parser)
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CELParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(CELParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CELParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested" ):
                listener.enterNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested" ):
                listener.exitNested(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested" ):
                return visitor.visitNested(self)
            else:
                return visitor.visitChildren(self)


    class IdentOrGlobalCallContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.PrimaryContext
            super().__init__(parser)
            self.leadingDot = None # Token
            self.id_ = None # Token
            self.op = None # Token
            self.args = None # ExprListContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(CELParser.IDENTIFIER, 0)
        def RPAREN(self):
            return self.getToken(CELParser.RPAREN, 0)
        def DOT(self):
            return self.getToken(CELParser.DOT, 0)
        def LPAREN(self):
            return self.getToken(CELParser.LPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(CELParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentOrGlobalCall" ):
                listener.enterIdentOrGlobalCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentOrGlobalCall" ):
                listener.exitIdentOrGlobalCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentOrGlobalCall" ):
                return visitor.visitIdentOrGlobalCall(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = CELParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 36]:
                localctx = CELParser.IdentOrGlobalCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 125
                    localctx.leadingDot = self.match(CELParser.DOT)


                self.state = 128
                localctx.id_ = self.match(CELParser.IDENTIFIER)
                self.state = 134
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 129
                    localctx.op = self.match(CELParser.LPAREN)
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135762105344) != 0):
                        self.state = 130
                        localctx.args = self.exprList()


                    self.state = 133
                    self.match(CELParser.RPAREN)


                pass
            elif token in [14]:
                localctx = CELParser.NestedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(CELParser.LPAREN)
                self.state = 137
                localctx.e = self.expr()
                self.state = 138
                self.match(CELParser.RPAREN)
                pass
            elif token in [10]:
                localctx = CELParser.CreateListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                localctx.op = self.match(CELParser.LBRACKET)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135762105344) != 0):
                    self.state = 141
                    localctx.elems = self.exprList()


                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 144
                    self.match(CELParser.COMMA)


                self.state = 147
                self.match(CELParser.RPRACKET)
                pass
            elif token in [12]:
                localctx = CELParser.CreateStructContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                localctx.op = self.match(CELParser.LBRACE)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135762105344) != 0):
                    self.state = 149
                    localctx.entries = self.mapInitializerList()


                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 152
                    self.match(CELParser.COMMA)


                self.state = 155
                self.match(CELParser.RBRACE)
                pass
            elif token in [18, 26, 27, 28, 31, 32, 33, 34, 35]:
                localctx = CELParser.ConstantLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.literal()
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


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext
            self.e = list() # of ExprContexts

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CELParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.COMMA)
            else:
                return self.getToken(CELParser.COMMA, i)

        def getRuleIndex(self):
            return CELParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = CELParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exprList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            localctx._expr = self.expr()
            localctx.e.append(localctx._expr)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.match(CELParser.COMMA)
                    self.state = 161
                    localctx._expr = self.expr()
                    localctx.e.append(localctx._expr) 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._IDENTIFIER = None # Token
            self.fields = list() # of Tokens
            self.s21 = None # Token
            self.cols = list() # of Tokens
            self._expr = None # ExprContext
            self.values = list() # of ExprContexts

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.IDENTIFIER)
            else:
                return self.getToken(CELParser.IDENTIFIER, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.COLON)
            else:
                return self.getToken(CELParser.COLON, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CELParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.COMMA)
            else:
                return self.getToken(CELParser.COMMA, i)

        def getRuleIndex(self):
            return CELParser.RULE_fieldInitializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldInitializerList" ):
                listener.enterFieldInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldInitializerList" ):
                listener.exitFieldInitializerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldInitializerList" ):
                return visitor.visitFieldInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def fieldInitializerList(self):

        localctx = CELParser.FieldInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fieldInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            localctx._IDENTIFIER = self.match(CELParser.IDENTIFIER)
            localctx.fields.append(localctx._IDENTIFIER)
            self.state = 168
            localctx.s21 = self.match(CELParser.COLON)
            localctx.cols.append(localctx.s21)
            self.state = 169
            localctx._expr = self.expr()
            localctx.values.append(localctx._expr)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 170
                    self.match(CELParser.COMMA)
                    self.state = 171
                    localctx._IDENTIFIER = self.match(CELParser.IDENTIFIER)
                    localctx.fields.append(localctx._IDENTIFIER)
                    self.state = 172
                    localctx.s21 = self.match(CELParser.COLON)
                    localctx.cols.append(localctx.s21)
                    self.state = 173
                    localctx._expr = self.expr()
                    localctx.values.append(localctx._expr) 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapInitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext
            self.keys = list() # of ExprContexts
            self.s21 = None # Token
            self.cols = list() # of Tokens
            self.values = list() # of ExprContexts

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CELParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.COLON)
            else:
                return self.getToken(CELParser.COLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CELParser.COMMA)
            else:
                return self.getToken(CELParser.COMMA, i)

        def getRuleIndex(self):
            return CELParser.RULE_mapInitializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapInitializerList" ):
                listener.enterMapInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapInitializerList" ):
                listener.exitMapInitializerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapInitializerList" ):
                return visitor.visitMapInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def mapInitializerList(self):

        localctx = CELParser.MapInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mapInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            localctx._expr = self.expr()
            localctx.keys.append(localctx._expr)
            self.state = 180
            localctx.s21 = self.match(CELParser.COLON)
            localctx.cols.append(localctx.s21)
            self.state = 181
            localctx._expr = self.expr()
            localctx.values.append(localctx._expr)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.match(CELParser.COMMA)
                    self.state = 183
                    localctx._expr = self.expr()
                    localctx.keys.append(localctx._expr)
                    self.state = 184
                    localctx.s21 = self.match(CELParser.COLON)
                    localctx.cols.append(localctx.s21)
                    self.state = 185
                    localctx._expr = self.expr()
                    localctx.values.append(localctx._expr) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CELParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BytesContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def BYTES(self):
            return self.getToken(CELParser.BYTES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBytes" ):
                listener.enterBytes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBytes" ):
                listener.exitBytes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBytes" ):
                return visitor.visitBytes(self)
            else:
                return visitor.visitChildren(self)


    class UintContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def NUM_UINT(self):
            return self.getToken(CELParser.NUM_UINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUint" ):
                listener.enterUint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUint" ):
                listener.exitUint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUint" ):
                return visitor.visitUint(self)
            else:
                return visitor.visitChildren(self)


    class NullContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(CELParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull" ):
                listener.enterNull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull" ):
                listener.exitNull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull" ):
                return visitor.visitNull(self)
            else:
                return visitor.visitChildren(self)


    class BoolFalseContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(CELParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolFalse" ):
                listener.enterBoolFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolFalse" ):
                listener.exitBoolFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolFalse" ):
                return visitor.visitBoolFalse(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CELParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class DoubleContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.sign = None # Token
            self.tok = None # Token
            self.copyFrom(ctx)

        def NUM_FLOAT(self):
            return self.getToken(CELParser.NUM_FLOAT, 0)
        def MINUS(self):
            return self.getToken(CELParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble" ):
                return visitor.visitDouble(self)
            else:
                return visitor.visitChildren(self)


    class BoolTrueContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.tok = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(CELParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolTrue" ):
                listener.enterBoolTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolTrue" ):
                listener.exitBoolTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolTrue" ):
                return visitor.visitBoolTrue(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CELParser.LiteralContext
            super().__init__(parser)
            self.sign = None # Token
            self.tok = None # Token
            self.copyFrom(ctx)

        def NUM_INT(self):
            return self.getToken(CELParser.NUM_INT, 0)
        def MINUS(self):
            return self.getToken(CELParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = CELParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = CELParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 192
                    localctx.sign = self.match(CELParser.MINUS)


                self.state = 195
                localctx.tok = self.match(CELParser.NUM_INT)
                pass

            elif la_ == 2:
                localctx = CELParser.UintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                localctx.tok = self.match(CELParser.NUM_UINT)
                pass

            elif la_ == 3:
                localctx = CELParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 197
                    localctx.sign = self.match(CELParser.MINUS)


                self.state = 200
                localctx.tok = self.match(CELParser.NUM_FLOAT)
                pass

            elif la_ == 4:
                localctx = CELParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                localctx.tok = self.match(CELParser.STRING)
                pass

            elif la_ == 5:
                localctx = CELParser.BytesContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                localctx.tok = self.match(CELParser.BYTES)
                pass

            elif la_ == 6:
                localctx = CELParser.BoolTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                localctx.tok = self.match(CELParser.TRUE)
                pass

            elif la_ == 7:
                localctx = CELParser.BoolFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 204
                localctx.tok = self.match(CELParser.FALSE)
                pass

            elif la_ == 8:
                localctx = CELParser.NullContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 205
                localctx.tok = self.match(CELParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.relation_sempred
        self._predicates[5] = self.calc_sempred
        self._predicates[7] = self.member_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_sempred(self, localctx:RelationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def calc_sempred(self, localctx:CalcContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def member_sempred(self, localctx:MemberContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




