#Stella Delia AM:2430
#Miltiadis Vasiliadis AM:2944

# Reserve Words
import sys
import os

PROGRAM_TK='programtk'
ENDPROGRAM_TK='endprogramtk'
DECLARATIONS_TK='declarationstk'
IF_TK='iftk'
THEN_TK='thentk'
ELSE_TK='elsetk'
ENDIF_TK='endiftk'
DO_TK='dotk'
WHILE_TK='whiletk'
ENDWHILE_TK='endwhiletk'
LOOPF_TK='loopforevertk'
ENDLOOP_TK='endlooptk'
EXIT_TK='exittk'
FORCASE_TK='forcasetk'
ENDFORCASE_TK='endforcasetk'
INCASE_TK='incasetk'
ENDINCASE_TK='endincasetk'
WHEN_TK='whentk'
DEFAULT_TK='defaulttk'
ENDDEFAULT_TK='enddefaulttk'
FUNCTION_TK='functiontk'
ENDFUNCTION_TK='endfunctiontk'
RETURN_TK='returntk'
IN_TK='intk'
INOUT_TK='inouttk'
INANDOUT_TK='inandouttk'
AND_TK='andtk'
OR_TK='ortk'
NOT_TK='nottk'
INPUT_TK='inputtk'
PRINT_TK='printtk'

ID_TK='idtk'
DIGIT_TK='digittk'
PLUS_TK='plustk'
MINUS_TK='minustk'
STAR_TK='startk'
SLASH_TK='slashtk'
OPENPAR_TK='openpartk'
CLOSEPAR_TK='closepartk'
OPENBRACKET_TK='openbrackettk'
CLOSEBRACKET_TK='closebrackettk'
SEMICOLON_TK='semicolontk'
COMMA_TK='commatk'
EQUAL_TK='equaltk'
ASSIGN_TK='assigntk'
COLON_TK='colontk'
DIF_TK='differenttk'
LESSOREQUAL_TK='smallorequaltk'
LESS_TK='smalltk'
GREATEROREQUAL_TK='greatorequaltk'
GREATER_TK='greattk'

state=0
line = 1
buffer="\0"*150
token=''
word=''

def getChar():
        c=f.read(1)
        return c

def backChar():
	f.seek(f.tell() - 1, os.SEEK_SET)

def isLetter(c):
	if (c>='A') and (c<='Z') or (c>='a') and (c<='z'):
		return True
	else:
		return False

def isDigit(c):
	if (c>='0') and (c<='9'):
		return True
	else:
		return False
		
def isSpace(c):
	if (c=='\n') or (c=='\t') or (c==' '):
		return True
	else:
		return False
		
		
def isNumOp(c):
	if c=='+' or c=='-' or c=='/' or c=='*':
		return True
	else:
		return False
		
def Reserved(word):
	
	word=''.join(word)
	if word=="program":
		return PROGRAM_TK,word
	if word=="endprogram":
		return ENDPROGRAM_TK,word
	if word=="declare":
		return DECLARATIONS_TK,word
	if word=="if":
		return IF_TK,word
	if word=="then":
		return THEN_TK,word
	if word=="else":
		return ELSE_TK,word
	if word=="endif":
		return ENDIF_TK
	if word=="do":
		return DO_TK,word
	if word=="while":
		return WHILE_TK,word
	if word=="endwhile":
		return ENDWHILE_TK,word
	if word=="loopf":
		return LOOPF_TK,word
	if word=="endloop":
		return ENDLOOP_TK,word
	if word=="exit":
		return EXIT_TK,word
	if word=="forcase":
		return FORCASE_TK,word
	if word=="endforcase":
		return ENDFORCASE_TK,word
	if word=="incase":
		return INCASE_TK,word
	if word=="endincase":
		return ENDINCASE_TK,word
	if  word=="when":
		return WHEN_TK,word
	if word=="default":
		return DEFAULT_TK,word
	if word=="enddefault":
		return ENDDEFAULT_TK,word
	if word=="function":
		return FUNCTION_TK,word
	if word=="endfunction":
		return ENDFUNCTION_TK,word
	if word=="return":
		return RETURN_TK,word
	if word=="in":
		return IN_TK,word
	if word=="inout":
		return INOUT_TK,word
	if word=="inandout":
		return INANDOUT_TK,word
	if word=="and":
		return AND_TK,word
	if word=="or":
		return OR_TK,word
	if word=="not":
		return NOT_TK,word
	if word=="input":
		return INPUT_TK,word
	if word=="print":
		return PRINT_TK,word
	else:
		return ID_TK,word
		
def lex():

	buffer = []
	
	while 1:
	
		c=getChar()
		if c=="\n":
			global line
			line+=1
		if isSpace(c):
			continue
			
		if isLetter(c):
			buffer.append(c)
			
			while 1:
				c=getChar()
				
				while isLetter(c) or isDigit(c):
					buffer.append(c)
					c=getChar()
				backChar()
				
				del buffer[30:]
				token, word = Reserved(buffer)
				#print(word)
				del buffer[:]
				return token,word
		
		if isDigit(c):
			buffer.append(c)
			c=getChar()
			while(isDigit(c)):
				buffer.append(c)
				c=getChar()
			
			word=''.join(buffer)
			int_work=int(word)
			if int_word <= 32767:
				backChar()
				token=DIGIT_TK
				return token, word
			else:
				print ('Number is out of limits! Error in line: %d ') %line
				exit(1)
		
		if c == '+':
			token=PLUS_TK
			return token,c
		
		if c == '-':
			token=MINUS_TK
			return token,c
			
		if c == '*':
			token=STAR_TK
			return token,c
			
		if c == '/':
			c=getChar()
			if c =='*':
				while 1:
					c=getChar()
					if c =='':
						print ('Error in comments: line : EOF',line)
						exit(1)
					if c=='*':
						c=getChar()
						if c =='/':
							token, word = lex()
							return token, word
						state=COMMENT_TK
			elif c=='/':
				while 1:
					c=getChar()
					if c=='\n':
						token, word = lex()
						return token, word
					state=COMMENT_TK
			else:
				backChar()
				token=SLASH_TK
				return token,c
		
		if c == '(':
			token=OPENPAR_TK
			return token,c
			
		if c == ')':
			token=CLOSEPAR_TK
			return token,c
			
		if c == '[':
			token=OPENBRACKET_TK
			return token,c
			
		if c == ']':
			token=CLOSEBRACKET_TK
			return token,c
			
		if c == ';':
			token=SEMICOLON_TK
			return token,c
			
		if c == ',':
			token=COMMA_TK
			return token,c
			
		if c == '=':
			token=EQUAL_TK
			return token,c
	
		if c == ':':
			c=getChar()
			if c =='=':
				token=ASSIGN_TK
				return token,':='
			else:
				backChar()
				token=COLON_TK
				return token,c
		
		if c == '<':
			c=getChar()
			if c=='>':
				token=DIF_TK
				return token,'<>'
			elif c=='=':
				token=LESSOREQUAL_TK
				return token,word
			else:
				backChar()
				token=LESS_TK
				return token,c
				
		if c=='>':
			c=getChar()
			if c =='=':
				token=GREATEROREQUAL_TK
				return token, '>='
			else:
				backChar()
				token=GREATER_TK
				return token,c
				
	else:
		print ('Found unrecognizable character in line %d!' %line)
		exit(0)
		
				
				
				
#syntax

def program():
	global token
	token,word=lex()
	#print(token)
	if token==PROGRAM_TK:
		token,word=lex()
		if token==ID_TK:
			token,word=lex();
			block();
		else :
			print ("Program Name expected at line",line)
			exit(0)
	else: 
		print("the keyword program was expected at line",line)
		exit(0)

def block():
	declarations()
	subprograms()
	statements()

def declarations():
	global token
	if token==DECLARATIONS_TK:
		varlist()
	else:
		print("Expected word 'declare' at line",line)
		exit(0)
		
def varlist():
	global token
	token,word=lex()
	if token==ID_TK:
		token,word=lex()
		while token==COMMA_TK:
			token,word=lex()
			if token!=ID_TK:
				print("Expected ID", line)
				exit(0)
			token,word=lex()
		if token!=SEMICOLON_TK:
			print("expected ; in line", line)
			exit(0)
	else:
		return

def subprograms():
	global token
	token,word=lex()
	print(token)
	while token==FUNCTION_TK:
		subprogram()
		token,word=lex()
	
def subprogram():
	global token	
	token,word=lex()
	if token!=ID_TK:
		print("error in line",line,"function id expected")
		exit()
	funcbody()
	
def funcbody():
	formalpars()
	block()

def formalpars():
	global token
	token,word=lex()
	print(token)
	if token!=OPENPAR_TK:
		print("error in line",line)
		exit(0)
	
	#token,word=lex()
	#if token==IN_TK or token==INANDOUT_TK or token==INOUT_TK:
	formalparlist()
		
	if token!=CLOSEPAR_TK:
		print("error, expected ')', line", line)
		exit(0)

def formalparlist():
	global token
	token,word=lex()
	if token==CLOSEPAR_TK:
		return
		
	formalparitem()
	token,word=lex()
	while token==COMMA_TK:	
		formalparitem()
		token,word=lex()
	return 		
	
def formalparitem():
	global token
	#token,word=lex()
	if token==IN_TK or token==INANDOUT_TK or token==INOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error, expected ID at line", line)
			exit(0)
	
def statements():
	global token
	statement()
	token,word=lex()
	if token==SEMICOLON_TK:
		statements()
	
def statement():
	global token
	
	if token==ID_TK:
		assignment_stat()
	if token==IF_TK:
		#token,word=lex()
		if_stat()
	if token==WHILE_TK:
		#token,word=lex()
		while_stat()
	if token==DO_TK:
		
		do_stat()
	if token==LOOPF_TK:
		
		loop_stat()
	if token==EXIT_TK:
		
		exit_stat()
	if token==FORCASE_TK:
	
		for_stat()
	
	if token==INCASE_TK:
		
		incase_stat()
		
	if token==RETURN_TK:
		
		return_stat()
	
	if token==INPUT_TK:
		
		input_stat()
		
	if token==PRINT_TK:
		
		print_stat()
		
	
def assignment_stat():
	global token
	token,word=lex()
	if token!=ID_TK:
		print("expected ID at line",line)
		exit(0)
	else:
		expression()
		
def if_stat():
	global token
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token,word=lex()
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
	token,word=lex()
	if token!=THEN_TK:
		print ('Expected thentk! error in line %d' %line)
		exit(0)
		
	statements()
	elsepart()
	token,word=lex()
	
	if token != ENDIF_TK :
		print ('Expected endiftk! error in line %d' %line)
		exit(0)
		
def else_part():
	global token
	token,word=lex()
	if token != ELSE_TK:
		print ('Expected elsetk! error in line %d' %line)
		exit(0)
	statements()
	
def while_stat():
	global token
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token,word=lex()
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
	statements()
	
	if token != ENDWHILE_TK :
		print ('Expected endwhiletk! error in line %d' %line)
		exit(0)
	
def do_while_stat():
	global token
	statements()
	token,word=lex()
	if token != WHILE_TK :
		print ('Expected whiletk! error in line %d' %line)
		exit(0)
		
	token,word=lex()	
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token,word=lex()
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
def loop_stat():
	global token
	statements()
	token,word=lex()
	if token != ENDLOOP_TK :
		print ('Expected endlooptk! error in line %d' %line)
		exit(0)
		
def exit_stat():
	global token
	token,word=lex()
	if token != EXIT_TK :
		print ('Expected exitptk! error in line %d' %line)
		exit(0)	

def forcase_stat():
	global token
	token,word=lex()
	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		condition()
		token,word=lex()
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
		statements()
		
	token,word=lex()
	if token!=DEFAULT_TK:
			print("Expected defaulttk! error in line",line)
			exit(0)
	if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
	statements()
	token,word=lex()
	if token!=ENDDEFAULT_TK:
			print("Expected enddefaulttk! error in line",line)
			exit(0)
	token,word=lex()
	if token!=ENDFORCASE_TK:
			print("Expected endforcasetk! error in line",line)
			exit(0)	
	
def incase_stat():
	global token
	token,word=lex()
	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		condition()
		token,word=lex()
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
		statements()
		
	token,word=lex()
	if token!=ENDINCASE_TK:
			print("Expected endincasetk! error in line",line)
			exit(0)	
	
def return_stat():
	global token
	token,word=lex()
	if token!=RETURN_TK:
			print("Expected returntk! error in line",line)
			exit(0)	

def print_stat():
	global token
	token,word=lex()
	#if token!=PRINT_TK:
	#		print("Expected printtk! error in line",line)
	#		exit(0)
	expression()

def input_stat():
	global token
	token,word=lex()
	#if token!=INPUT_TK:
	#	print("Expected word 'input' at line,"line)
	#	exit(0)
	if token!=ID_TK:
		print("Expected ID at line,", line)
		exit(0)
		
def actualpars():
	global token
	#token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected ( at line,",line)
		exit(0)
	actualparlist()
	
	if token!=CLOSEPAR_TK:
		print("expected ) at line", line)
	
def actualparlist():
	global token
	token,word=lex()
	if token!=CLOSEPAR_TK:
		actualparitem()
		token,word=lex()
		while token==COMMA_TK:
			actualparitem()
			token,word=lex()
	else:
		return

def actualparitem():
	global token
	token,word=lex()
	if token==IN_TK:
		expression()
	elif token==INOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
	elif token==INANDOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
	else:
		print("error actual par item",line)

def condition():
	global token
	boolterm()
	token,word=lex()
	while token==OR_TK:
		boolterm()
		token,word=lex()
def boolterm():
	global token
	boolfactor()
	token,word=lex()
	while token==AND_TK:
		boolfactor()
		token,word=lex()
def boolfactor():
	global token
	token,word=lex()
	if token==NOT_TK:
		token,word=lex()
		if token==OPENBRACKET_TK:
			condition()
		
		else:
			print("expected [ at line",line)
			exit(0)
		token,word=lex()	
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
	elif token==OPENBRACKET_TK:
		condition()
		token,word=lex()
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
	else:
		expression()
		relational_oper()
		expression()
		
def expression():
	global token
	optional_sign()
	term()
	token,word=lex()
	while(token==PLUS_TK or token==MINUS_TK):
		add_oper()
		term()
		token,word=lex()

def term():
	global token
	factor()
	token,word=lex()
	while(token==STAR_TK or token==SLASH_TK):
		mul_oper()
		factor()
		token,word=lex()
		
def factor():
	global token
	if token==DIGIT_TK():
		return
	elif token==OPENPAR_TK:
		expression()
		token,word=lex()
		if token!=CLOSEPAR_TK:
			print("expected ) at line", line)
			exit(0)
	elif token==ID_TK:
		idtail()
	else: 
		print("error in factor", line)
		
def idtail():
	global token
	token,word=lex()
	if token==OPENBRACKET_TK:
		actualpars()
	else:
		return

def relational_oper():
	global token
	if token==EQUAL_TK:
		token,word=lex()
	if token==LESSOREQUAL_TK:
		token,word=lex()
	if token==GREATEROREQUAL_TK:
		token,word=lex()
	if token==LESS_TK:
		token,word=lex()
	if token==GREATER_TK:
		token,word=lex()
	if token==DIF_TK:
		token,word=lex()
	else:
		print("expected = <= >= <> < >", line)
		exit(0)
		
def add_oper():
	global token
	if token==PLUS_TK:
		token,word=lex()
	if token==MINUS_TK:
		token,word=lex()
	else:
		print("expected, + or - ", line)
		exit(0)
		
def mul_oper():
	global token
	if token==STAR_TK:
		token,word=lex()
	if token==SLASH_TK:
		token,word=lex()
	else:
		print("expected * or /", line)
		
def optional_sign():
	global token
	lex()

f=open(sys.argv[1],"r")
program()
