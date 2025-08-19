# Generated from Calculator.g4 by ANTLR 4.13.2
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
        4,1,16,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,3,
        0,28,8,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,5,6,60,8,6,10,6,12,6,63,9,6,1,7,1,7,1,7,5,7,68,8,7,10,7,12,
        7,71,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,79,8,8,1,8,0,0,9,0,2,4,6,8,
        10,12,14,16,0,2,1,0,7,8,1,0,9,10,81,0,23,1,0,0,0,2,35,1,0,0,0,4,
        37,1,0,0,0,6,40,1,0,0,0,8,44,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,
        14,64,1,0,0,0,16,78,1,0,0,0,18,19,3,2,1,0,19,20,5,6,0,0,20,22,1,
        0,0,0,21,18,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,
        27,1,0,0,0,25,23,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,27,28,1,0,0,
        0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,36,3,4,2,0,32,36,3,
        6,3,0,33,36,3,8,4,0,34,36,3,12,6,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,1,0,0,38,39,5,14,0,
        0,39,5,1,0,0,0,40,41,5,14,0,0,41,42,5,5,0,0,42,43,3,12,6,0,43,7,
        1,0,0,0,44,45,5,2,0,0,45,46,3,10,5,0,46,47,5,3,0,0,47,50,3,2,1,0,
        48,49,5,4,0,0,49,51,3,2,1,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,
        0,0,52,53,3,12,6,0,53,54,5,13,0,0,54,55,3,12,6,0,55,11,1,0,0,0,56,
        61,3,14,7,0,57,58,7,0,0,0,58,60,3,14,7,0,59,57,1,0,0,0,60,63,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,13,1,0,0,0,63,61,1,0,0,0,64,69,
        3,16,8,0,65,66,7,1,0,0,66,68,3,16,8,0,67,65,1,0,0,0,68,71,1,0,0,
        0,69,67,1,0,0,0,69,70,1,0,0,0,70,15,1,0,0,0,71,69,1,0,0,0,72,79,
        5,15,0,0,73,79,5,14,0,0,74,75,5,11,0,0,75,76,3,12,6,0,76,77,5,12,
        0,0,77,79,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,74,1,0,0,0,79,17,
        1,0,0,0,7,23,27,35,50,61,69,78
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'if'", "'then'", "'else'", "'='", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "VAR", "IF", "THEN", "ELSE", "ASSIGN", 
                      "SEMI", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", "RPAREN", 
                      "REL_OP", "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_comando = 1
    RULE_declaracao = 2
    RULE_atribuicao = 3
    RULE_estruturaIf = 4
    RULE_comparacao = 5
    RULE_expressao = 6
    RULE_termo = 7
    RULE_fator = 8

    ruleNames =  [ "prog", "comando", "declaracao", "atribuicao", "estruturaIf", 
                   "comparacao", "expressao", "termo", "fator" ]

    EOF = Token.EOF
    VAR=1
    IF=2
    THEN=3
    ELSE=4
    ASSIGN=5
    SEMI=6
    PLUS=7
    MINUS=8
    MUL=9
    DIV=10
    LPAREN=11
    RPAREN=12
    REL_OP=13
    ID=14
    NUMBER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalculatorParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ComandoContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.SEMI)
            else:
                return self.getToken(CalculatorParser.SEMI, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalculatorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 18
                    self.comando()
                    self.state = 19
                    self.match(CalculatorParser.SEMI) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 51206) != 0):
                self.state = 26
                self.comando()


            self.state = 29
            self.match(CalculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_comando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EstruturaIfCmdContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def estruturaIf(self):
            return self.getTypedRuleContext(CalculatorParser.EstruturaIfContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstruturaIfCmd" ):
                listener.enterEstruturaIfCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstruturaIfCmd" ):
                listener.exitEstruturaIfCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstruturaIfCmd" ):
                return visitor.visitEstruturaIfCmd(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracaoCmdContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaracao(self):
            return self.getTypedRuleContext(CalculatorParser.DeclaracaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoCmd" ):
                listener.enterDeclaracaoCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoCmd" ):
                listener.exitDeclaracaoCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoCmd" ):
                return visitor.visitDeclaracaoCmd(self)
            else:
                return visitor.visitChildren(self)


    class ExpressaoCmdContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(CalculatorParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoCmd" ):
                listener.enterExpressaoCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoCmd" ):
                listener.exitExpressaoCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoCmd" ):
                return visitor.visitExpressaoCmd(self)
            else:
                return visitor.visitChildren(self)


    class AtribuicaoCmdContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atribuicao(self):
            return self.getTypedRuleContext(CalculatorParser.AtribuicaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicaoCmd" ):
                listener.enterAtribuicaoCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicaoCmd" ):
                listener.exitAtribuicaoCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicaoCmd" ):
                return visitor.visitAtribuicaoCmd(self)
            else:
                return visitor.visitChildren(self)



    def comando(self):

        localctx = CalculatorParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CalculatorParser.DeclaracaoCmdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.declaracao()
                pass

            elif la_ == 2:
                localctx = CalculatorParser.AtribuicaoCmdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.atribuicao()
                pass

            elif la_ == 3:
                localctx = CalculatorParser.EstruturaIfCmdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.estruturaIf()
                pass

            elif la_ == 4:
                localctx = CalculatorParser.ExpressaoCmdContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.expressao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalculatorParser.VAR, 0)

        def ID(self):
            return self.getToken(CalculatorParser.ID, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = CalculatorParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CalculatorParser.VAR)
            self.state = 38
            self.match(CalculatorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculatorParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CalculatorParser.ASSIGN, 0)

        def expressao(self):
            return self.getTypedRuleContext(CalculatorParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = CalculatorParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CalculatorParser.ID)
            self.state = 41
            self.match(CalculatorParser.ASSIGN)
            self.state = 42
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstruturaIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CalculatorParser.IF, 0)

        def comparacao(self):
            return self.getTypedRuleContext(CalculatorParser.ComparacaoContext,0)


        def THEN(self):
            return self.getToken(CalculatorParser.THEN, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ComandoContext,i)


        def ELSE(self):
            return self.getToken(CalculatorParser.ELSE, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_estruturaIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstruturaIf" ):
                listener.enterEstruturaIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstruturaIf" ):
                listener.exitEstruturaIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstruturaIf" ):
                return visitor.visitEstruturaIf(self)
            else:
                return visitor.visitChildren(self)




    def estruturaIf(self):

        localctx = CalculatorParser.EstruturaIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_estruturaIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CalculatorParser.IF)
            self.state = 45
            self.comparacao()
            self.state = 46
            self.match(CalculatorParser.THEN)
            self.state = 47
            self.comando()
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(CalculatorParser.ELSE)
                self.state = 49
                self.comando()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExpressaoContext,i)


        def REL_OP(self):
            return self.getToken(CalculatorParser.REL_OP, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_comparacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacao" ):
                listener.enterComparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacao" ):
                listener.exitComparacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacao" ):
                return visitor.visitComparacao(self)
            else:
                return visitor.visitChildren(self)




    def comparacao(self):

        localctx = CalculatorParser.ComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expressao()
            self.state = 53
            self.match(CalculatorParser.REL_OP)
            self.state = 54
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.TermoContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.TermoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.PLUS)
            else:
                return self.getToken(CalculatorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MINUS)
            else:
                return self.getToken(CalculatorParser.MINUS, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = CalculatorParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.termo()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 57
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                self.termo()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.FatorContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.FatorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MUL)
            else:
                return self.getToken(CalculatorParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.DIV)
            else:
                return self.getToken(CalculatorParser.DIV, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = CalculatorParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.fator()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 65
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.fator()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculatorParser.NUMBER, 0)

        def ID(self):
            return self.getToken(CalculatorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CalculatorParser.LPAREN, 0)

        def expressao(self):
            return self.getTypedRuleContext(CalculatorParser.ExpressaoContext,0)


        def RPAREN(self):
            return self.getToken(CalculatorParser.RPAREN, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = CalculatorParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fator)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(CalculatorParser.NUMBER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(CalculatorParser.ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(CalculatorParser.LPAREN)
                self.state = 75
                self.expressao()
                self.state = 76
                self.match(CalculatorParser.RPAREN)
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





