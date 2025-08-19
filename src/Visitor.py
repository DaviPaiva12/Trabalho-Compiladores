from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor

class EvalVisitor(CalculatorVisitor):
    def __init__(self):
        self.variables = {}

    def visitProg(self, ctx:CalculatorParser.ProgContext):
        last_result = None
        for cmd_ctx in ctx.comando():
            last_result = self.visit(cmd_ctx)
        return last_result

    def visitDeclaracaoCmd(self, ctx:CalculatorParser.DeclaracaoCmdContext):
        var_name = ctx.declaracao().ID().getText()
        self.variables[var_name] = 0.0
        return f"Variável '{var_name}' declarada."

    def visitAtribuicaoCmd(self, ctx:CalculatorParser.AtribuicaoCmdContext):
        var_name = ctx.atribuicao().ID().getText()
        if var_name not in self.variables:
            raise NameError(f"Erro: Variável '{var_name}' não foi declarada.")
        value = self.visit(ctx.atribuicao().expressao())
        self.variables[var_name] = value
        return value

    def visitExpressaoCmd(self, ctx:CalculatorParser.ExpressaoCmdContext):
        return self.visit(ctx.expressao())

    def visitEstruturaIfCmd(self, ctx:CalculatorParser.EstruturaIfCmdContext):
        condicao_result = self.visit(ctx.estruturaIf().comparacao())
        if condicao_result:
            return self.visit(ctx.estruturaIf().comando(0))
        elif ctx.estruturaIf().comando(1):
            return self.visit(ctx.estruturaIf().comando(1))

    def visitComparacao(self, ctx:CalculatorParser.ComparacaoContext):
        left = self.visit(ctx.expressao(0))
        right = self.visit(ctx.expressao(1))
        op = ctx.REL_OP().getText()

        if op == '<': return left < right
        if op == '>': return left > right
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<=': return left <= right
        if op == '>=': return left >= right

    def visitFator(self, ctx:CalculatorParser.FatorContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            raise NameError(f"Erro: Variável '{var_name}' não declarada.")
        if ctx.expressao():
            return self.visit(ctx.expressao())

    def visitTermo(self, ctx:CalculatorParser.TermoContext):
        result = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            op = ctx.getChild(i * 2 - 1).getText()
            right = self.visit(ctx.fator(i))
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ValueError("Erro: Divisão por zero.")
                result /= right
        return result

    def visitExpressao(self, ctx:CalculatorParser.ExpressaoContext):
        result = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            op = ctx.getChild(i * 2 - 1).getText()
            right = self.visit(ctx.termo(i))
            if op == '+':
                result += right
            else:
                result -= right
        return result