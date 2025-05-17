# Generated from Math.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("D\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4O\n\4\f\4")
        buf.write("\16\4R\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6[\n\6\f\6\16")
        buf.write("\6^\13\6\3\7\3\7\3\7\3\7\3\7\5\7e\n\7\3\7\2\3\6\b\2\4")
        buf.write("\6\b\n\f\2\4\3\2\3\4\3\2\5\6\2p\2\16\3\2\2\2\4\23\3\2")
        buf.write("\2\2\6C\3\2\2\2\bS\3\2\2\2\nW\3\2\2\2\fd\3\2\2\2\16\17")
        buf.write("\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\24\5\6\4\2\22\24")
        buf.write("\5\b\5\2\23\21\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\25\26")
        buf.write("\b\4\1\2\26\27\7\b\2\2\27\30\7\t\2\2\30\31\5\6\4\2\31")
        buf.write("\32\7\n\2\2\32D\3\2\2\2\33\34\7\13\2\2\34\35\7\t\2\2\35")
        buf.write("\36\5\6\4\2\36\37\7\n\2\2\37D\3\2\2\2 !\7\f\2\2!\"\7\t")
        buf.write("\2\2\"#\5\6\4\2#$\7\n\2\2$D\3\2\2\2%&\7\r\2\2&\'\7\t\2")
        buf.write("\2\'(\5\6\4\2()\7\n\2\2)D\3\2\2\2*+\7\16\2\2+,\7\t\2\2")
        buf.write(",-\5\6\4\2-.\7\n\2\2.D\3\2\2\2/\60\7\17\2\2\60\61\7\t")
        buf.write("\2\2\61\62\5\6\4\2\62\63\7\n\2\2\63D\3\2\2\2\64\65\7\17")
        buf.write("\2\2\65\66\7\t\2\2\66\67\5\6\4\2\678\7\20\2\289\7\23\2")
        buf.write("\29:\7\n\2\2:D\3\2\2\2;<\7\t\2\2<=\5\6\4\2=>\7\n\2\2>")
        buf.write("D\3\2\2\2?@\7\4\2\2@D\5\6\4\5AD\7\23\2\2BD\7\24\2\2C\25")
        buf.write("\3\2\2\2C\33\3\2\2\2C \3\2\2\2C%\3\2\2\2C*\3\2\2\2C/\3")
        buf.write("\2\2\2C\64\3\2\2\2C;\3\2\2\2C?\3\2\2\2CA\3\2\2\2CB\3\2")
        buf.write("\2\2DP\3\2\2\2EF\f\20\2\2FG\t\2\2\2GO\5\6\4\21HI\f\17")
        buf.write("\2\2IJ\t\3\2\2JO\5\6\4\20KL\f\16\2\2LM\7\7\2\2MO\5\6\4")
        buf.write("\17NE\3\2\2\2NH\3\2\2\2NK\3\2\2\2OR\3\2\2\2PN\3\2\2\2")
        buf.write("PQ\3\2\2\2Q\7\3\2\2\2RP\3\2\2\2ST\7\21\2\2TU\5\n\6\2U")
        buf.write("V\7\22\2\2V\t\3\2\2\2W\\\5\f\7\2XY\7\20\2\2Y[\5\f\7\2")
        buf.write("ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\13\3\2\2\2")
        buf.write("^\\\3\2\2\2_`\7\21\2\2`a\5\n\6\2ab\7\22\2\2be\3\2\2\2")
        buf.write("ce\7\23\2\2d_\3\2\2\2dc\3\2\2\2e\r\3\2\2\2\b\23CNP\\d")
        return buf.getvalue()


class MathParser ( Parser ):

    grammarFileName = "Math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'**'", "'exp'", 
                     "'('", "')'", "'sqrt'", "'sin'", "'cos'", "'tan'", 
                     "'log'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "VARIABLE", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_function = 2
    RULE_matrix = 3
    RULE_row = 4
    RULE_element = 5

    ruleNames =  [ "program", "expression", "function", "matrix", "row", 
                   "element" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    NUMBER=17
    VARIABLE=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MathParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(MathParser.EOF, 0)

        def getRuleIndex(self):
            return MathParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MathParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expression()
            self.state = 13
            self.match(MathParser.EOF)
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

        def function(self):
            return self.getTypedRuleContext(MathParser.FunctionContext,0)


        def matrix(self):
            return self.getTypedRuleContext(MathParser.MatrixContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MathParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MathParser.T__1, MathParser.T__5, MathParser.T__6, MathParser.T__8, MathParser.T__9, MathParser.T__10, MathParser.T__11, MathParser.T__12, MathParser.NUMBER, MathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.function(0)
                pass
            elif token in [MathParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.matrix()
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.FunctionContext)
            else:
                return self.getTypedRuleContext(MathParser.FunctionContext,i)


        def NUMBER(self):
            return self.getToken(MathParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(MathParser.VARIABLE, 0)

        def getRuleIndex(self):
            return MathParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)



    def function(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.FunctionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_function, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(MathParser.T__5)
                self.state = 21
                self.match(MathParser.T__6)
                self.state = 22
                self.function(0)
                self.state = 23
                self.match(MathParser.T__7)
                pass

            elif la_ == 2:
                self.state = 25
                self.match(MathParser.T__8)
                self.state = 26
                self.match(MathParser.T__6)
                self.state = 27
                self.function(0)
                self.state = 28
                self.match(MathParser.T__7)
                pass

            elif la_ == 3:
                self.state = 30
                self.match(MathParser.T__9)
                self.state = 31
                self.match(MathParser.T__6)
                self.state = 32
                self.function(0)
                self.state = 33
                self.match(MathParser.T__7)
                pass

            elif la_ == 4:
                self.state = 35
                self.match(MathParser.T__10)
                self.state = 36
                self.match(MathParser.T__6)
                self.state = 37
                self.function(0)
                self.state = 38
                self.match(MathParser.T__7)
                pass

            elif la_ == 5:
                self.state = 40
                self.match(MathParser.T__11)
                self.state = 41
                self.match(MathParser.T__6)
                self.state = 42
                self.function(0)
                self.state = 43
                self.match(MathParser.T__7)
                pass

            elif la_ == 6:
                self.state = 45
                self.match(MathParser.T__12)
                self.state = 46
                self.match(MathParser.T__6)
                self.state = 47
                self.function(0)
                self.state = 48
                self.match(MathParser.T__7)
                pass

            elif la_ == 7:
                self.state = 50
                self.match(MathParser.T__12)
                self.state = 51
                self.match(MathParser.T__6)
                self.state = 52
                self.function(0)
                self.state = 53
                self.match(MathParser.T__13)
                self.state = 54
                self.match(MathParser.NUMBER)
                self.state = 55
                self.match(MathParser.T__7)
                pass

            elif la_ == 8:
                self.state = 57
                self.match(MathParser.T__6)
                self.state = 58
                self.function(0)
                self.state = 59
                self.match(MathParser.T__7)
                pass

            elif la_ == 9:
                self.state = 61
                self.match(MathParser.T__1)
                self.state = 62
                self.function(3)
                pass

            elif la_ == 10:
                self.state = 63
                self.match(MathParser.NUMBER)
                pass

            elif la_ == 11:
                self.state = 64
                self.match(MathParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.FunctionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_function)
                        self.state = 67
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 68
                        _la = self._input.LA(1)
                        if not(_la==MathParser.T__0 or _la==MathParser.T__1):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.function(15)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.FunctionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_function)
                        self.state = 70
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 71
                        _la = self._input.LA(1)
                        if not(_la==MathParser.T__2 or _la==MathParser.T__3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.function(14)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.FunctionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_function)
                        self.state = 73
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")

                        self.state = 74
                        self.match(MathParser.T__4)
                        self.state = 75
                        self.function(13)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(MathParser.RowContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)




    def matrix(self):

        localctx = MathParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MathParser.T__14)
            self.state = 82
            self.row()
            self.state = 83
            self.match(MathParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.ElementContext)
            else:
                return self.getTypedRuleContext(MathParser.ElementContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = MathParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.element()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MathParser.T__13:
                self.state = 86
                self.match(MathParser.T__13)
                self.state = 87
                self.element()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(MathParser.RowContext,0)


        def NUMBER(self):
            return self.getToken(MathParser.NUMBER, 0)

        def getRuleIndex(self):
            return MathParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = MathParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_element)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MathParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(MathParser.T__14)
                self.state = 94
                self.row()
                self.state = 95
                self.match(MathParser.T__15)
                pass
            elif token in [MathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(MathParser.NUMBER)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.function_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def function_sempred(self, localctx:FunctionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         




