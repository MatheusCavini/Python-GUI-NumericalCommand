grammar GCode;

gcode
    :	statement+ fimprograma
	;
	
fimprograma 
	:	numerolinha mfim
	;
		
statement 
	:	numerolinha codfunc coordx? coordy? fimdelinha
	|	numerolinha mfunc fimdelinha
	|   fimdelinha
	;

numerolinha 
	:	'N'INT INT INT?
	;

mfim
    :	'M30'
	;
	
mfunc 
	:	'M02'
	|	'M01' STRING
	;
	
codfunc
    :	'G01'
	|	'G00'
	;
	
coordx
    :	'X'coord
	;

coordy
    :	'Y'coord
	;
		
coord
    :
    '-'? INT INT? INT?
	;

fimdelinha
    :	'\r'
	|	'\n'
	|   '\r\n'
	;
			
INT
    :	'0'..'9'
    ;
	
ID  : 'a'..'z'  ;
WS  : [ \t\n\r]+-> skip ;
	
STRING
    :  '"' ( ~('\\'|'"') )* '"'
    ;

