# Generated from Regex.g4 by ANTLR 4.13.2
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
        4,1,8,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,4,2,23,8,2,11,2,12,2,24,
        1,3,1,3,3,3,29,8,3,1,4,1,4,1,4,1,4,1,4,3,4,36,8,4,1,4,0,0,5,0,2,
        4,6,8,0,1,1,0,3,5,36,0,10,1,0,0,0,2,13,1,0,0,0,4,22,1,0,0,0,6,26,
        1,0,0,0,8,35,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,
        18,3,4,2,0,14,15,5,2,0,0,15,17,3,4,2,0,16,14,1,0,0,0,17,20,1,0,0,
        0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,18,1,0,0,0,21,23,3,
        6,3,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,
        5,1,0,0,0,26,28,3,8,4,0,27,29,7,0,0,0,28,27,1,0,0,0,28,29,1,0,0,
        0,29,7,1,0,0,0,30,31,5,6,0,0,31,32,3,2,1,0,32,33,5,7,0,0,33,36,1,
        0,0,0,34,36,5,1,0,0,35,30,1,0,0,0,35,34,1,0,0,0,36,9,1,0,0,0,4,18,
        24,28,35
    ]

class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|'", "'*'", "'+'", "'?'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "CHAR", "PIPE", "STAR", "PLUS", "QMARK", 
                      "LPAREN", "RPAREN", "WS" ]

    RULE_regex = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_base = 4

    ruleNames =  [ "regex", "expression", "term", "factor", "base" ]

    EOF = Token.EOF
    CHAR=1
    PIPE=2
    STAR=3
    PLUS=4
    QMARK=5
    LPAREN=6
    RPAREN=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RegexParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(RegexParser.EOF, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression()
            self.state = 11
            self.match(RegexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AlternationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.TermContext)
            else:
                return self.getTypedRuleContext(RegexParser.TermContext,i)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(RegexParser.PIPE)
            else:
                return self.getToken(RegexParser.PIPE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternation" ):
                listener.enterAlternation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternation" ):
                listener.exitAlternation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternation" ):
                return visitor.visitAlternation(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = RegexParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            localctx = RegexParser.AlternationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.term()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 14
                self.match(RegexParser.PIPE)
                self.state = 15
                self.term()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConcatenationContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.FactorContext)
            else:
                return self.getTypedRuleContext(RegexParser.FactorContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatenation" ):
                listener.enterConcatenation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatenation" ):
                listener.exitConcatenation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation" ):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = RegexParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            localctx = RegexParser.ConcatenationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.factor()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QuantifiersContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def base(self):
            return self.getTypedRuleContext(RegexParser.BaseContext,0)

        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)
        def PLUS(self):
            return self.getToken(RegexParser.PLUS, 0)
        def QMARK(self):
            return self.getToken(RegexParser.QMARK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifiers" ):
                listener.enterQuantifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifiers" ):
                listener.exitQuantifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantifiers" ):
                return visitor.visitQuantifiers(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = RegexParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        self._la = 0 # Token type
        try:
            localctx = RegexParser.QuantifiersContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.base()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 27
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_base

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GroupContext(BaseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.BaseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RegexParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(RegexParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(RegexParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)


    class CharacterContext(BaseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.BaseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(RegexParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter" ):
                listener.enterCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter" ):
                listener.exitCharacter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacter" ):
                return visitor.visitCharacter(self)
            else:
                return visitor.visitChildren(self)



    def base(self):

        localctx = RegexParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_base)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = RegexParser.GroupContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(RegexParser.LPAREN)
                self.state = 31
                self.expression()
                self.state = 32
                self.match(RegexParser.RPAREN)
                pass
            elif token in [1]:
                localctx = RegexParser.CharacterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(RegexParser.CHAR)
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





