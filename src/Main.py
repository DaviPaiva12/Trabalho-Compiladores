import sys
from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from Visitor import EvalVisitor

def main():
    print("Calculadora Simples com ANTLR")
    print("Digite 'sair' para terminar.")

    while True:
        try:
            text = input(">> ")
            if text.lower() == 'sair':
                break
            if not text:
                continue

            input_stream = InputStream(text)
            lexer = CalculatorLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = CalculatorParser(stream)
            tree = parser.prog()

            visitor = EvalVisitor()
            result = visitor.visit(tree)
            
            print(f"Resultado: {result}")

        except (ValueError, SyntaxError, NameError) as e:
            print(e)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    main()