# Trabalho de Compiladores: Calculadora Simples

**Nome:** Davi Nunes de Paiva  
**RA:** 11202231636

## Visão Geral

Este projeto foi desenvolvido для a disciplina de Compiladores e segue a Modalidade Individual, cujo objetivo é a criação de uma calculadora simples. A ferramenta principal utilizada para a análise sintática foi o ANTLR, e a linguagem de programação do interpretador é Python.

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
Tokens Principais
Categoria	Tokens
Palavras-Chave	var, if, then, else
Operadores	=, +, -, *, /, <, >, ==, !=, <=, >=
Literais e ID	NUMBER (números), ID (variáveis)
Símbolos	(, ), ;

Exportar para as Planilhas
Tutorial de Utilização
Siga os passos abaixo para configurar o ambiente e executar o compilador.

Pré-requisitos
Antes de começar, garanta que você tenha instalado:

Python 3

Java Development Kit (JDK) (versão 8 ou superior)

Configuração do Ambiente
Clone ou Baixe o Repositório: Certifique-se de que todos os arquivos do projeto estejam em uma mesma pasta.

Baixe o ANTLR: Faça o download do arquivo antlr-4.x.x-complete.jar do site oficial do ANTLR e coloque-o na pasta do projeto.

Instale o Runtime do ANTLR para Python: Abra um terminal na pasta do projeto e execute:

Bash

pip install antlr4-python3-runtime
Gere o Parser: Ainda no terminal, execute o comando abaixo. Lembre-se de ajustar o nome do arquivo .jar para a versão que você baixou.

Bash

java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 grammar/Calculator.g4 -visitor
Execução do Compilador
Com o ambiente configurado, execute o script principal para iniciar a calculadora interativa:

Bash

py -m src.Main
O programa exibirá um prompt >> aguardando seus comandos. Para encerrar, digite sair.

Exemplos de Uso
Operações Matemáticas
PowerShell

>> 10 + 2 * 5
Resultado: 20.0

>> (10 + 2) * 3
Resultado: 36.0

>> 15 / 2
Resultado: 7.5
Uso de Variáveis
PowerShell

>> var x;
Resultado: Variável 'x' declarada.

>> x = 100 / 4;
Resultado: 25.0

>> x * 2 + 1
Resultado: 51.0
Estrutura if-then-else
PowerShell

>> var nota;
Resultado: Variável 'nota' declarada.

>> nota = 7.5;
Resultado: 7.5

>> if nota > 7 then 1 else 0
Resultado: 1.0
Tratamento de Erros
PowerShell

>> y = 50
Erro: Variável 'y' não foi declarada.

>> 10 * (5 +
line 1:10 missing ')' at '<EOF>'
Resultado: None
