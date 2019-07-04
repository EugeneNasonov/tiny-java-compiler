grammar gmar;

program : mainClass classDecl*;
mainClass : 'class' identifier '{' mainMethod '}';
mainMethod : 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}';
classBody : fieldDecl* methodDecl* ;
classDecl : 'class' identifier '{' classBody '}';
methodDecl : vartype identifier '(' paramList ')' '{' methodBody '}';
fieldDecl : vartype identifier SEMICOLON;
identifier: IDENTIFIER;
methodBody: fieldDecl*	statement* returnStatement;

statement
	: '{' statement* '}' #blockStatement
	| 'while' '(' expression ')' statement #whileStatement
	| 'do' statement 'while' '(' expression ')' SEMICOLON #doWhileStatement
	| 'if' '(' expression ')' statement ('else' statement)? #ifStatement
	| (identifier '=')+ expression SEMICOLON #assignStatement
	| 'System.out.println' '(' expression ')' SEMICOLON #printStatement
	| 'break' SEMICOLON #breakStatement
	| 'continue' SEMICOLON #breakStatement
	| identifier '[' expression ']' '=' expression SEMICOLON #assignArrayStatement
	;
returnStatement
	: 'return' expression SEMICOLON ;

paramList : parameters? ;
parameters : parameter ( ',' parameter )*;
parameter : vartype identifier;

expression:
    conjunction ('||' conjunction)* #disjunctionExpression
    ;

conjunction: equality ('&&' equality)* #conjunctionExpression;
equality: comparison ('==' equality)* #equalExpression
        | comparison ('!=' equality)* #notEqualExpression
        ;
comparison: sigma ('<' comparison)* #ltExpression
          | sigma ('>' comparison)* #gtExpression
          | sigma ('<=' comparison)* #leExpression
          | sigma ('>=' comparison)* #geExpression
          ;
sigma: product ('+' sigma)* #sumExpression
   | product ('-' sigma)* #subtractExpression
   ;
product: factor ('*' product)* #mulExpression
       | factor ('/' product)* #divExpression
       ;

factor: '!' factor #notExpression
      | '-' factor #minusExpression
      | '+' factor #plusExpression
      |	atom '[' expression ']'  #arraySelectExpression
      | atom '.' 'length' #arrayLengthExpression
      |	atom '.' methodCall ('.' methodCall)?	#methodCallExpression
	  | atom '.' identifier #variableCallExpression
      | atom #factorToAtomExpression
      ;

atom: integral #integerExpression
    | boolean  #boolExpression
    | character #charExpression
    | identifier #identifierExpression
    | 'this' #thisExpression
    | 'new' identifier '(' ')' #newCallExpression
    | 'new' 'int' '[' expression ']' #arrayCreateExpression
    | '(' expression ')' #bracketExpression
   ;


methodCall: identifier '(' (expression (',' expression)*)? ')' ;

integral: INTEGER;
boolean: BOOLEAN;
character: CHAR;

vartype
	: identifier
	| integralType
	| integralArrayType
	| characterType
	| booleanType
	;
integralType: 'int';
integralArrayType: 'int' '['']' ;
characterType: 'char';
booleanType: 'boolean';

LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' .*? '*/' -> skip;
INTEGER: ('0'..'9')+ ;
BOOLEAN: 'true' | 'false';
CHAR: '\'' .  '\'';
SEMICOLON  : ';';
IDENTIFIER
	: ('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;
WS: [ \t\r\n]+ -> skip;