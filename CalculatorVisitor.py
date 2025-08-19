# Generated from Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#prog.
    def visitProg(self, ctx:CalculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#DeclaracaoCmd.
    def visitDeclaracaoCmd(self, ctx:CalculatorParser.DeclaracaoCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#AtribuicaoCmd.
    def visitAtribuicaoCmd(self, ctx:CalculatorParser.AtribuicaoCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#EstruturaIfCmd.
    def visitEstruturaIfCmd(self, ctx:CalculatorParser.EstruturaIfCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ExpressaoCmd.
    def visitExpressaoCmd(self, ctx:CalculatorParser.ExpressaoCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#declaracao.
    def visitDeclaracao(self, ctx:CalculatorParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#atribuicao.
    def visitAtribuicao(self, ctx:CalculatorParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#estruturaIf.
    def visitEstruturaIf(self, ctx:CalculatorParser.EstruturaIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#comparacao.
    def visitComparacao(self, ctx:CalculatorParser.ComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#expressao.
    def visitExpressao(self, ctx:CalculatorParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#termo.
    def visitTermo(self, ctx:CalculatorParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#fator.
    def visitFator(self, ctx:CalculatorParser.FatorContext):
        return self.visitChildren(ctx)



del CalculatorParser