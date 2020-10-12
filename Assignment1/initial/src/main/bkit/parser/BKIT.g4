grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : ;


//3.3 TOKEN SET
//--3.3.1--IDENTIFIERS
ID: [a-z][a-zA-Z0-9_]*;
//--3.3.2--KEYWORDS
BODY:'Body';
BREAK:'Break';
DO:'Do';
ENDDO:'EndDo';
CONTINUE:'Continue';
IF:'If';
ELSEIF:'ElseIf';
ELSE:'Else';
ENDBODY:'EndBody';
ENDIF:'EndIf';
FOR:'For';
ENDFOR:'EndFor';
WHILE:'While';
ENDWHILE:'EndWhile';
FUNCTION:'Function';
PARAMETER:'Parameter';
RETURN:'Return';
THEN:'Then';
VAR:'Var';
TRUE:'True';
FALSE:'False';
   
//--3.3.3--OPERATORS------
//-------ARITHMETIC OPERATORS--------
//-------ARITHMETIC OPERATORS INTERGER-------
SUB:'-';
ADD:'+';
MUL:'*';
DIV:'\\';
RM:'%';
//-------ARITHMETIC OPERATORS FLOAT-------
SUBFLT:'-.';
ADDFLT:'+.';
MULFLT:'*.';
DIVFLT:'\\.';
//------------BOOLEN TYPE----------------
NEG: '!';
CONJ:'&&';
DISJ:'||';
//------------RELATIONAL OPERATORS----------
//------------RELATIONAL OPERATORS INTEGER----------
EQ:'==';
NEQ:'!=';
LES:'<';
GRE:'>';
LESEQ:'<=';
GREEQ:'>=';
//------------RELATIONAL OPERATORS FLOAT----------
NEQFLT:'=/=';
LESSFLT:'<.';
GREFLT:'>.';
LESEQFLT:'<=.';
GREEQFLT:'>=.';
//--3.3.4---SEPARATORS---
LP:'('; //Left Parenthesis
RP:')';//Right Parenthesis
LSB:'['; //Left Square Bracket
RSB:']';//Right Square Bracket
LCB:'{';//Left Curly Bracket
RCB:'}';//Right Curly Bracket
SEMI:';';
COLON:':';
COMMA:',';
DOT:'.'; 
//--3.3.5--LITERAL
//INTERGER
INTERGER_LITERAL: HEX|OCT|DEC;
fragment DEC: '0'|[1-9][0-9]*;
fragment HEX: ('0x'|'0X')[0-9A-F]+;
fragment OCT: ('0o'|'0O')[0-7]+;
//FLOAT
FLOAT_LITERAL:INT_PART DEC_PART EXP_PART;
fragment INT_PART:[0-9]+;
fragment DEC_PART:'.'[0-9]*;
fragment EXP_PART: ('e'|'E')[+-][0-9]+;
//BOOLEAN
BOOLEAN_LITERAL:TRUE|FALSE;
//STRING_LITERAL
STRING_LITERAL:'"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* '"';
//ARRAY_LITERAL



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;