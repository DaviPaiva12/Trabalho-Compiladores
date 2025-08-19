# Generated from Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#prog.
    def enterProg(self, ctx:CalculatorParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculatorParser#prog.
    def exitProg(self, ctx:CalculatorParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculatorParser#DeclaracaoCmd.
    def enterDeclaracaoCmd(self, ctx:CalculatorParser.DeclaracaoCmdContext):
        pass

    # Exit a parse tree produced by CalculatorParser#DeclaracaoCmd.
    def exitDeclaracaoCmd(self, ctx:CalculatorParser.DeclaracaoCmdContext):
        pass


    # Enter a parse tree produced by CalculatorParser#AtribuicaoCmd.
    def enterAtribuicaoCmd(self, ctx:CalculatorParser.AtribuicaoCmdContext):
        pass

    # Exit a parse tree produced by CalculatorParser#AtribuicaoCmd.
    def exitAtribuicaoCmd(self, ctx:CalculatorParser.AtribuicaoCmdContext):
        pass


    # Enter a parse tree produced by CalculatorParser#EstruturaIfCmd.
    def enterEstruturaIfCmd(self, ctx:CalculatorParser.EstruturaIfCmdContext):
        pass

    # Exit a parse tree produced by CalculatorParser#EstruturaIfCmd.
    def exitEstruturaIfCmd(self, ctx:CalculatorParser.EstruturaIfCmdContext):
        pass


    # Enter a parse tree produced by CalculatorParser#ExpressaoCmd.
    def enterExpressaoCmd(self, ctx:CalculatorParser.ExpressaoCmdContext):
        pass

    # Exit a parse tree produced by CalculatorParser#ExpressaoCmd.
    def exitExpressaoCmd(self, ctx:CalculatorParser.ExpressaoCmdContext):
        pass


    # Enter a parse tree produced by CalculatorParser#declaracao.
    def enterDeclaracao(self, ctx:CalculatorParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by CalculatorParser#declaracao.
    def exitDeclaracao(self, ctx:CalculatorParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by CalculatorParser#atribuicao.
    def enterAtribuicao(self, ctx:CalculatorParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CalculatorParser#atribuicao.
    def exitAtribuicao(self, ctx:CalculatorParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CalculatorParser#estruturaIf.
    def enterEstruturaIf(self, ctx:CalculatorParser.EstruturaIfContext):
        pass

    # Exit a parse tree produced by CalculatorParser#estruturaIf.
    def exitEstruturaIf(self, ctx:CalculatorParser.EstruturaIfContext):
        pass


    # Enter a parse tree produced by CalculatorParser#comparacao.
    def enterComparacao(self, ctx:CalculatorParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by CalculatorParser#comparacao.
    def exitComparacao(self, ctx:CalculatorParser.ComparacaoContext):
        pass


    # Enter a parse tree produced by CalculatorParser#expressao.
    def enterExpressao(self, ctx:CalculatorParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expressao.
    def exitExpressao(self, ctx:CalculatorParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by CalculatorParser#termo.
    def enterTermo(self, ctx:CalculatorParser.TermoContext):
        pass

    # Exit a parse tree produced by CalculatorParser#termo.
    def exitTermo(self, ctx:CalculatorParser.TermoContext):
        pass


    # Enter a parse tree produced by CalculatorParser#fator.
    def enterFator(self, ctx:CalculatorParser.FatorContext):
        pass

    # Exit a parse tree produced by CalculatorParser#fator.
    def exitFator(self, ctx:CalculatorParser.FatorContext):
        pass



del CalculatorParser