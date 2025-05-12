grammar Math;

options {language=Java;}

program: expression EOF;

expression: function | matrix;       // for choosing specific domain

// Function for Calculus domain

function:
    function ('+' | '-') function       // additive
|   function ('*' | '/') function       // multiplicative
|   function ('**') function            // power
|   'exp' '(' function ')'              // natural exponentiation
|   'sqrt' '(' function ')'             // square root
|   'sin' '(' function ')'              // sin
|   'cos' '(' function ')'              // cos
|   'tan' '(' function ')'              // tan
|   'log' '(' function ')'              // natural log
|   'log' '(' function ',' NUMBER ')'     // base log
|   '(' function ')'                    // parens
|   '-' function                        // unary minus
|   NUMBER
|   VARIABLE;

// Matrix for Linear domain

matrix: '[' row ']';       // for starting a new 2d matrix

row: element (',' element)*;

element: '[' row ']' | NUMBER;

// Tokens
NUMBER: [0-9]+ ('.' [0-9]+)?;           // e.g: 1, 11, 11.11, etc

VARIABLE: [a-zA-Z][a-zA-Z0-9]*;         // e.g: a, a1, aA, aA1, etc

WS: [ \t\r\n]+ -> skip;                 // skip whitespace, newline, etc
