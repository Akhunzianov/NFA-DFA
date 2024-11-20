grammar Regex;

regex: expression EOF;

expression
    : term (PIPE term)*    # Alternation
    ;

term
    : factor+              # Concatenation
    ;

factor
    : base (STAR | PLUS | QMARK)?  # Quantifiers
    ;

base
    : LPAREN expression RPAREN    # Group
    | CHAR                         # Character
    ;

CHAR    : [a-zA-Z0-9];
PIPE    : '|';
STAR    : '*';
PLUS    : '+';
QMARK   : '?';
LPAREN  : '(';
RPAREN  : ')';
WS      : [ \t\r\n]+ -> skip;