# Trabalho de Compiladores: Calculadora Simples

**Nome:** Davi Nunes de Paiva
**RA:** 11202231636

## Visão Geral

Este projeto foi desenvolvido para a disciplina de Compiladores e segue a Modalidade Individual, cujo objetivo é a criação de uma calculadora simples. A ferramenta principal utilizada para a análise sintática foi o ANTLR, e a linguagem de programação do interpretador é Python.

## Recursos Implementados

O compilador atende a todos os requisitos mínimos para a modalidade, que incluem:

-   **Expressões Matemáticas**: Suporte completo a operações de `+`, `-`, `*`, `/`, respeitando a precedência matemática correta.
-   **Números Decimais**: Capacidade de processar e calcular com números de ponto flutuante (reais).
-   **Variáveis**: Permite a declaração e atribuição de variáveis.
-   **Verificação de Declaração**: O compilador verifica se uma variável foi declarada antes de ser utilizada.
-   **Estrutura de Controle**: Implementação da estrutura condicional `if ... then ... else`.
-   **Feedback ao Usuário**: Retorna o valor calculado em caso de sucesso ou uma mensagem de erro explicativa para erros de sintaxe ou semântica.

## Gramática e Tokens

A gramática utilizada foi projetada para não conter recursividade à esquerda, conforme solicitado nas instruções.

### Gramática
```antlr
prog: (comando SEMI)* comando? EOF;
comando: declaracao | atribuicao | estruturaIf | expressao;
declaracao: VAR ID;
atribuicao: ID ASSIGN expressao;
estruturaIf: IF comparacao THEN comando (ELSE comando)?;
comparacao: expressao REL_OP expressao;
expressao: termo ( (PLUS | MINUS) termo )*;
termo:     fator ( (MUL | DIV) fator )*;
fator:     NUMBER | ID | LPAREN expressao RPAREN;

