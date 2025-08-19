grammar Calculator;

prog: (comando SEMI)* comando? EOF;

comando
    : declaracao      # DeclaracaoCmd
    | atribuicao      # AtribuicaoCmd
    | estruturaIf     # EstruturaIfCmd
    | expressao       # ExpressaoCmd
    ;

declaracao: VAR ID;
atribuicao: ID ASSIGN expressao;

estruturaIf:
    IF comparacao THEN comando (ELSE comando)?
    ;

comparacao: expressao REL_OP expressao;

expressao: termo ( (PLUS | MINUS) termo )*;
termo:     fator ( (MUL | DIV) fator )*;
fator:
    NUMBER
    | ID
    | LPAREN expressao RPAREN
    ;

//TOKENS
VAR: 'var';
IF: 'if';
THEN: 'then';
ELSE: 'else';
ASSIGN: '=';
SEMI: ';';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
REL_OP: '<' | '>' | '==' | '!=' | '<=' | '>=';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;