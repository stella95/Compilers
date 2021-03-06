def program()
	token=lex()
	if token==PROGRAM_TK:
		token=lex()
		if token==ID_TK:
			token=lex();
			block();
		else :
			print ("Program Name expected at line",line)
			exit(0)
	else: 
		error("the keyword program was expected at line,line)
		exit(0)

def block()
	declarations()
	subprograms()
	statements()

def declarations()
	if token==DECLARATIONS_TK:
		varlist()
	else:
		print("Expected word 'declare' at line",line)
		exit(0)
		
def varlist()
	varlist()
	token=lex()
	while token==COMMA_TK:
		token=lex()
		
		if token!=ID_TK:
		print("Expected ID", line)
		exit(0)
	else:
		return

def subprograms()
	while token==FUNCTION_TK:
		subprogram()
		token=lex()
	
def subprogram()
	token=lex()
	if token!=ID_TK:
		print("error in line",line,"function id expected")
		exit()
	funcbody()
	
def funcbody()
	formalpars()
	block()

def formalpars()
	token=lex()
	if token!=OPENPAR_TK:
		print("error in line",line)
		exit(0)
	token=lex()
	if token==IN_TK or token==INANDOUT_TK or token==INOUT_TK:
		formalparlist()
		
	token=lex()
	if token!=CLOSEPAR_TK:
		print("error, expected ')', line" line)
		exit(0)

def formalparlist()
	token=lex()
	formalparitem()
	token=lex()
	while token=COMMA_TK:
		
		formalparitem()
		token=lex()
	return token		
	
def formalparitem()
	if token!=ID_TK:
		print("error, expected ID at line", line)
		exit(0)
	
def statements()
	statement()
	token=lex()
	if token==SEMICOLON_TK:
		statements()
	
def statement()
	
	if token==ID_TK:
		#token=lex()
	if token==IF_STAT:
		#token=lex()
		if_stat()
	if token==WHILE_TK:
		#token=lex()
		while_stat()
	if token==DO_TK:
		
		do_stat()
	if token==LOOPF_TK:
		
		loop_stat()
	if token==EXIT_TK:
		
		exit_stat()
	if token==FOR_TK:
	
		for_stat()
	
	if token==INCASE_TK:
		
		incase_stat()
		
	if token==RETURN_TK:
		
		return_stat()
	
	if token==INPUT_TK:
		
		input_stat()
		
	if token==PRINT_TK:
		
		print_stat()
		
	
def assignment_stat()
	token=lex()
	if token!=ID_TK:
		print("expected ID at line",line)
		exit(0)
	else:
		expression()
		
def if_stat()
	token=lex()	
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token=lex()
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
	token=lex()
	if token!=THEN_TK:
		print 'Expected thentk! error in line %d' %line
		exit(0)
		
	statements()
	elsepart()
	token=lex()
	
	if token != ENDIF_TK :
		print 'Expected endiftk! error in line %d' %line
		exit(0)
		
def else_part()
	token=lex()
	if token != ELSE_TK:
		print 'Expected elsetk! error in line %d' %line
		exit(0)
	statements()
	
def while_stat()
	token=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token=lex()
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
	statements()
	
	if token != ENDWHILE_TK :
		print 'Expected endwhiletk! error in line %d' %line
		exit(0)
	
def do_while_stat()	
	statements()
	token=lex()
	if token != WHILE_TK :
		print 'Expected whiletk! error in line %d' %line
		exit(0)
		
	token=lex()	
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	condition()
	token=lex()
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	
def loop_stat()
	statements()
	token=lex()
	if token != ENDLOOP_TK :
		print 'Expected endlooptk! error in line %d' %line
		exit(0)
		
def exit_stat()
	token=lex()
	if token != EXIT_TK :
		print 'Expected exitptk! error in line %d' %line
		exit(0)	

def forcase_stat()
	token=lex()
	while token== WHEN_TK:
		token=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		condition()
		token=lex()
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
		statements()
		
	token=lex()
	if token!=DEFAULT_TK:
			print("Expected defaulttk! error in line",line)
			exit(0)
	if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
	statements()
	token=lex()
	if token!=ENDDEFAULT_TK:
			print("Expected enddefaulttk! error in line",line)
			exit(0)
	token=lex()
	if token!=ENDFORCASE_TK:
			print("Expected endforcasetk! error in line",line)
			exit(0)	
	
def incase_stat()
	token=lex()
	while token== WHEN_TK:
		token=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		condition()
		token=lex()
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
			
		statements()
		
	token=lex()
	if token!=ENDINCASE_TK:
			print("Expected endincasetk! error in line",line)
			exit(0)	
	
def return_stat()
	token=lex()
	if token!=RETURN_TK:
			print("Expected returntk! error in line",line)
			exit(0)	

def print_stat()
	token=lex()
	#if token!=PRINT_TK:
	#		print("Expected printtk! error in line",line)
	#		exit(0)
	expression()

def input_stat()
	token=lex()
	#if token!=INPUT_TK:
	#	print("Expected word 'input' at line,"line)
	#	exit(0)
	if token!=ID_TK
		print("Expected ID at line,", line)
		exit(0)
		
def actualpars()
	#token=lex()
	if token!=OPENPAR_TK:
		print("Expected ( at line,",line)
		exit(0)
	actualparlist()
	
	if token!=CLOSEPAR_TK:
		print("expected ) at line", line)
	
def actualparlist()
	token=lex()
	if token!=CLOSEPAR_TK:
		actualparitem()
		token=lex()
		while token==COMMA_TK
			actualparitem()
			token=lex()
	else:
		return

def actualparitem()
	token=lex()
	if token==IN_TK:
		expression()
	elif token==INOUT_TK:
		token=lex()
		if token!=ID_TK:
		print("error expected ID", line)
		exit(0)
	elif token==INANDOUT_TK
		token=lex()
		if token!=ID_TK:
		print("error expected ID", line)
		exit(0)
	else:
		print("error actual par item",line)

def condition()
	boolterm()
	token=lex()
	while token==OR_TK:
		boolterm()
		token=lex()
def boolterm()
	boolfactor()
	token=lex()
	while token==AND_TK:
		boolfactor()
		token=lex()
def boolfactor()
	token=lex()
	if token==NOT_TK:
		token=lex()
		if token==OPENBRACKET_TK:
			condition()
		
		else:
			print("expected [ at line",line)
			exit(0)
		token=lex()	
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
	elif token==OPENBRACKET_TK:
		condition()
		token=lex()
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
	else:
		expression()
		relational_oper()
		expression()
		
def expression()
	optional_sign()
	term()
	token=lex()
	while(token==PLUS_TK or token==MINUS_TK):
		add_oper()
		term()
		token=lex()

def term()
	factor()
	token=lex()
	while(token==STAR_TK or token==SLASH_TK):
		mul_oper()
		factor()
		token=lex()
		
def factor()
	if token==DIGIT_TK():
		
	elif token==OPENPAR_TK:
		expression()
		token=lex()
		if token!=CLOSEPAR_TK:
			print("expected ) at line", line)
			exit(0)
	elif token==ID_TK:
		idtail()
	else: 
		print("error in factor", line)
		
def idtail()
	token=lex()
	if token==OPENBRACKET_TK:
		actualpars()
	else:
		return

def relational_oper()
	if token==EQUAL_TK:
		
	if token==LESSOREQUAL_TK:
		
	if token==GREATEROREQUAL_TK:
	
	if token==LESS_TK:
	
	if token==GREATER_TK:
	
	if token==DIF_TK:
	
	else:
		print("expected = <= >= <> < >", line)
		exit(0)
		
def add_oper()
	if token==PLUS_TK:
	
	if token==MINUS_TK:
	
	else:
		print("expected, + or - ", line)
		exit(0)
		
def mul_oper()
	if token==STAR_TK:
	
	if token==SLASH_TK:
	
	else:
		print("expected * or /", line)
		
def optional_sign()
	try:
		add_oper()
	except:
		
	finally:
	
	