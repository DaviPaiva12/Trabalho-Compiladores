# Trabalho de Compiladores: Calculadora Simples

**Nome:** Davi Nunes de Paiva
**RA:** 11202231636

## Visão Geral

Este projeto foi desenvolvido para a disciplina de Compiladores e segue a Modalidade Individual, cujo objetivo é a criação de uma calculadora simples. A ferramenta principal utilizada para a análise sintática foi o ANTLR, e a linguagem de programação do interpretador é Python.

## Recursos Implementados

-   **Expressões Matemáticas**: Suporte completo a operações de `+`, `-`, `*`, `/`, respeitando a precedência matemática correta.
-   **Números Decimais**: Capacidade de processar e calcular com números de ponto flutuante (reais).
-   **Variáveis**: Permite a declaração e atribuição de variáveis.
-   **Verificação de Declaração**: O compilador verifica se uma variável foi declarada antes de ser utilizada.
-   **Estrutura de Controle**: Implementação da estrutura condicional `if ... then ... else`.
-   **Feedback ao Usuário**: Retorna o valor calculado em caso de sucesso ou uma mensagem de erro explicativa para erros de sintaxe ou semântica.

## Gramática e Tokens

### Gramática
- `prog: (comando SEMI)* comando? EOF;`
- `comando: declaracao | atribuicao | estruturaIf | expressao;`
- `declaracao: VAR ID;`
- `atribuicao: ID ASSIGN expressao;`
- `estruturaIf: IF comparacao THEN comando (ELSE comando)?;`
- `comparacao: expressao REL_OP expressao;`
- `expressao: termo ( (PLUS | MINUS) termo )*;`
- `termo: fator ( (MUL | DIV) fator )*;`
- `fator: NUMBER | ID | LPAREN expressao RPAREN;`

### Tokens Principais
-   `Palavras-Chave`: `var`, `if`, `then`, `else`
-   `Operadores`: `=`, `+`, `-`, `*`, `/`, `<`, `>`, `==`, `!=`, `<=`, `>=`
-   `Literais e ID`: `NUMBER` (números), `ID` (variáveis)
-   `Símbolos`: `(`, `)`, `;`

## Tutorial de Utilização

Siga os passos abaixo para configurar o ambiente e executar o compilador.

### Pré-requisitos
-   Python 3
-   Java Development Kit (JDK) (versão 8 ou superior)

### Configuração do Ambiente
1.  **Clone ou Baixe o Repositório**: Certifique-se de que todos os arquivos do projeto estejam em uma mesma pasta.
2.  **Baixe o ANTLR**: Faça o download do arquivo `antlr-4.x.x-complete.jar` do [site oficial do ANTLR](https://www.antlr.org/download.html) e coloque-o na pasta do projeto.
3.  **Instale o Runtime do ANTLR para Python**: Abra um terminal na pasta do projeto e execute:
    ```bash
    pip install antlr4-python3-runtime
    ```
4.  **Gere o Parser**: Ainda no terminal, execute o comando abaixo. Lembre-se de ajustar o nome do arquivo `.jar` para a versão que você baixou.
    ```bash
    java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 grammar/Calculator.g4 -visitor
    ```

### Execução do Compilador
Com o ambiente configurado, execute o script principal para iniciar a calculadora interativa:
```bash
py -m src.Main
