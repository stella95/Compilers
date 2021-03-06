#Stella Delia AM:2430 username: cse32430
#Miltiadis Vasiliadis AM:2944 username:cse52944

# Reserve Words
import sys
import os
import symbol

PROGRAM_TK='programtk'
ENDPROGRAM_TK='endprogramtk'
DECLARE_TK='declaretk'
IF_TK='iftk'
THEN_TK='thentk'
ELSE_TK='elsetk'
ENDIF_TK='endiftk'
DOWHILE_TK='dotk'
WHILE_TK='whiletk'
ENDWHILE_TK='endwhiletk'
ENDDOWHILE_TK='enddowhiletk'
LOOP_TK='looptk'
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
tempCounter=0
label=0
programID=''
r=0
#gia to loop ston endiameso
exitID=''
exitHelp=[]
inter=0

symboltable = []
currentdepth = -1
finalcode = ["L:j Lmain"]

#classes gia pinaka symbolon


class entity:
	name = ''
	type = ''
	offset = 0


	startquad = -1
	arguments = []
	framelength = -1
	parMode = ''
	value = ''
	startquad = ''
	nextEntity = None
	def __init__(self,n,t):
		name = n
		type = t



class scope:
	Entities = []

	nestingLevel=0
	enclosingScope= None
	baseOffset = 12
	def __init__(self):
		nestingLevel=0

class argument:
	parmode = ''

	type = ''
	next= None
	def __init__(self,par):
		parmode=par
 ##SYNARTISEIS GIA TON ENDIAMESO KODIKA##

def nextQuad():
	global label
	return label

def emptyList():
	return []

def newTemp():
	global tempCounter
	t='T_'+str(tempCounter)
	tempCounter=tempCounter+1
	return t

def genQuad(oper,x,y,z):
	global label
	global intermediate
	lbl = str(label)
	quad = [lbl, oper, x, y, z]
	label = label + 1

	intermediate = intermediate + [quad]

def makeList(x):
	z=str(x)
	return[z]

def mergeList(L1,L2):
	return L1+L2

def backpatch(L,z):
	z = str(z)
	global intermediate
	label=L[0]
	for i in range(len(intermediate)):
		x = intermediate[i]
		if x[0] == label:
			x[4] = z
			break



# Endiamesos

intermediate= emptyList()
variables= emptyList()

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
		return DECLARE_TK,word
	if word=="if":
		return IF_TK,word
	if word=="then":
		return THEN_TK,word
	if word=="else":
		return ELSE_TK,word
	if word=="endif":
		return ENDIF_TK,word
	if word=="dowhile":
		return DOWHILE_TK,word
	if word=="while":
		return WHILE_TK,word
	if word=="enddowhile":
		return ENDDOWHILE_TK,word
	if word=="endwhile":
		return ENDWHILE_TK,word
	if word=="loop":
		return LOOP_TK,word
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
				#print(*buffer)
				token, word = Reserved(buffer)
				del buffer[:]
				return token,word

		if isDigit(c):
			buffer.append(c)
			c=getChar()
			if isLetter(c):
				print('Error in lex ids cant start with digit at line', line )
				exit(0)
			while(isDigit(c)):
				buffer.append(c)
				c=getChar()
				if isLetter(c):
					print('Error in lex ids cant start with digit at line', line )
					exit(0)

			word=''.join(buffer)

			int_word=int(word)
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
						#state=COMMENT_TK
			elif c=='/':
				while 1:
					c=getChar()
					if c=='\n':
						token, word = lex()
						return token, word
					#state=COMMENT_TK
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
				return token,":"

		if c == '<':
			c=getChar()
			if c=='>':
				token=DIF_TK
				return token,'<>'
			elif c=='=':
				token=LESSOREQUAL_TK
				return token,'<='
			else:
				backChar()
				token=LESS_TK
				return token,"<"

		if c=='>':
			c=getChar()
			if c =='=':
				token=GREATEROREQUAL_TK
				return token, '>='
			else:
				backChar()
				token=GREATER_TK
				return token,">"

	else:
		print ('Found unrecognizable character in line %d!' %line)
		exit(0)




#syntax

def program():
	global token
	global word
	token,word=lex()
	if token==PROGRAM_TK:
		#new_scope()
		token,word=lex()
		if token==ID_TK:
			global programID
			programID=word
			genQuad("begin_block",word , "_", "_")
			token,word=lex()
			block()
		else:
			print ("Program Name expected at line",line)
			exit(0)
	else:
		print("the keyword program was expected at line",line)
		exit(0)
	if token!=ENDPROGRAM_TK:
		print("ERROR expected endprogram at line",line)
		exit(0)
	else:
		print('SyntaxPassed')
		#exit(0)
	#delete_scope()
	genQuad("halt", "_","_", "_")
	genQuad("end_block",programID,"_","_")

def block():
	global token
	global word
	declarations()
	subprograms()
	statements()

def declarations():
	global token
	global word
	if token==DECLARE_TK:
		token,word=lex()
		varlist()
		if token!=SEMICOLON_TK:
			print("expected ; in line", line)
			exit(0)
		token,word=lex()
	else:
		return

def varlist():
	global token
	global word
	if token==ID_TK:
		token,word=lex()
		#new_entity(word,ID_TK)
		while token==COMMA_TK:
			token,word=lex()
			if token!=ID_TK:
				print("Expected ID", line)
				exit(0)
			token,word=lex()
	else:
		return

def subprograms():
	global token
	global word
	while token==FUNCTION_TK:
		token,word=lex()
		global functionID
		functionID=word
		subprogram(functionID)

def subprogram(name):
	global token
	global word
	#add_scope()
	#new_entity(word,FUNCTION_TK,)		 		
	if token!=ID_TK:
		print("error in line",line,"function id expected")
		exit(0)
	genQuad("begin_block",name , "_", "_")
	token,word=lex()
	funcbody()
	if token!=ENDFUNCTION_TK:
		print("error in line",line,"endfunction expected")
		exit(0)
	#delete_scope()
	genQuad("end_block",name,"_","_")
	token,word=lex()

def funcbody():
	global token
	global word
	formalpars()
	block()

def formalpars():
	global token
	global word
	if token!=OPENPAR_TK:
		print("error in line",line)
		exit(0)

	token,word=lex()
	formalparlist()

	if token!=CLOSEPAR_TK:
		print("error, expected ')', line", line)
		exit(0)
	token,word=lex()

def formalparlist():
	global token
	global word
	if token==CLOSEPAR_TK:
		return

	formalparitem()

	while token==COMMA_TK:
		token,word=lex()
		formalparitem()
	return

def formalparitem():
	global token
	global word
	if token==IN_TK:
		token,word=lex()
		#add_entity(word,IN_TK)
		#add_argument(word,IN_TK)
		if token!=ID_TK:
			print("error, expected ID at line", line)
			exit(0)
		genQuad("par",word,"CV","_")
		token,word=lex()
	elif token==INOUT_TK:
		token,word=lex()
		#add_entity(word,IN_TK)
		#add_argument(word,IN_TK)				  
		if token!=ID_TK:
			print("error expected IDat line", line)
			exit(0)
		genQuad("par",word,"REF","_")
		token,word=lex()
	elif token==INANDOUT_TK:
		token,word=lex()
		#add_entity(word,IN_TK)
		#add_argument(word,IN_TK)				  
		if token!=ID_TK:
			print("error expected ID at line", line)
			exit(0)
		genQuad("par",word,"RET","_")
		token,word=lex()
	else:
		print("error formal par item",line)
		exit(0)

def statements():
	global token
	global word
	statement()
	while token==SEMICOLON_TK:
		token,word=lex()
		statement()

def statement():
	global token
	global word
	if token==ID_TK:
		assignment_stat(word)
	elif token==IF_TK:

		if_stat()
	elif token==WHILE_TK:

		while_stat()
	elif token==DOWHILE_TK:

		dowhile_stat()
	elif token==LOOP_TK:

		loop_stat()
	elif token==EXIT_TK:
		exit_stat()
	elif token==FORCASE_TK:

		for_stat()

	elif token==INCASE_TK:

		incase_stat()

	elif token==RETURN_TK:

		return_stat()

	elif token==INPUT_TK:

		input_stat()

	elif token==PRINT_TK:

		print_stat()
	else:
		return

def assignment_stat(IDPlace):
	global token
	global word
	EPlace=""

	token,word=lex()

	if token!=ASSIGN_TK:
		print("expected := at line",line)
		exit(0)
	token,word=lex()
	EPlace=expression()
	genQuad(":=", EPlace, "_", IDPlace)

def if_stat():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	ifList=emptyList()
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()
	BTrue,BFalse=condition()

	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()

	if token!=THEN_TK:
		print ('Expected thentk! error in line %d' %line)
		exit(0)
	token,word=lex()
	backpatch(BTrue,nextQuad())
	statements()
	ifList=makeList(nextQuad())
	genQuad("jump", "_", "_", "_")
	backpatch(BFalse, nextQuad())
	else_part()
	backpatch(ifList, nextQuad())

	if token != ENDIF_TK :
		print ('Expected endiftk! error in line %d' %line)
		exit(0)
	token,word=lex()

def else_part():
	global token
	global word
	if token == ELSE_TK:
		token,word=lex()
		statements()

def while_stat():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()
	Bquad=nextQuad()
	BTrue,BFalse=condition()

	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()
	backpatch(BTrue,nextQuad())

	statements()
	genQuad("jump", "_", "_",str(Bquad))
	backpatch(BFalse, nextQuad())

	if token != ENDWHILE_TK :
		print ('Expected endwhiletk! error in line %d' %line)
		exit(0)
	token,word=lex()

def dowhile_stat():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	token,word=lex()
	sQuad=nextQuad()
	statements()

	if token != ENDDOWHILE_TK :
		print ('Expected whiletk! error in line %d' %line)
		exit(0)
	token,word=lex()

	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()

	BTrue,BFalse=condition()

	backpatch(BFalse, str(sQuad))
	backpatch(BTrue, nextQuad())

	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()

def loop_stat():
	global token
	global word
	global exitID
	global exitHelp
	global inter
	sQuad=nextQuad()
	token,word=lex()
	statements()
	genQuad("jump","_","_",str(sQuad))

	if token != ENDLOOP_TK :
		print ('Expected endlooptk! error in line %d' %line)
		exit(0)
	token,word=lex()

	if (exitID=='true'):
                backpatch(intermediate[exitHelp[inter-1]],nextQuad())
                inter=inter-1

def exit_stat():
	global token
	global word
	global exitID
	global exitHelp
	global inter
	exitID='true'
	genQuad("jump","_","_","_")
	exitHelp.append(len(intermediate)-1)
	inter=inter+1
	token,word=lex()
	return

def for_stat():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	token,word=lex()
	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		sQuad=nextQuad()
		BTrue,BFalse=condition()

		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()

		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
		token,word=lex()
		backpatch(BTrue,nextQuad())
		statements()
		genQuad("jump", "_", "_", str(sQuad))
		backpatch(BFalse,nextQuad())

	if token!=DEFAULT_TK:
			print("Expected defaulttk! error in line",line)
			exit(0)
	token,word=lex()

	if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
	token,word=lex()
	statements()
	genQuad("jump", "_", "_", "_")

	if token!=ENDDEFAULT_TK:
			print("Expected enddefaulttk! error in line",line)
			exit(0)
	token,word=lex()

	if token!=ENDFORCASE_TK:
			print("Expected endforcasetk! error in line",line)
			exit(0)
	token,word=lex()

def incase_stat():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	token,word=lex()

	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		sQuad=nextQuad()
		BTrue,BFalse=condition()

		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()

		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
		token,word=lex()
		backpatch(BTrue,nextQuad())
		statements()
		genQuad("jump", "_", "_", str(sQuad))
		backpatch(BFalse,nextQuad())

	if token!=ENDINCASE_TK:
			print("Expected endincasetk! error in line",line)
			exit(0)
	token,word=lex()

def return_stat():
	global token
	global word
	EPlace=""
	token,word=lex()
	EPlace=expression()
	genQuad("retv",EPlace,"_","_")

def print_stat():
	global token
	global word
	EPlace=""
	token,word=lex()
	EPlace=expression()
	genQuad("out",EPlace,"_","_")

def input_stat():
	global token
	global word
	token,word=lex()
	idPlace=word
	if token!=ID_TK:
		print("Expected ID at line,", line)
		exit(0)
	genQuad("inp",idPlace,"_","_")
	token,word=lex()

def actualpars():
	global token
	global word
	if token!=OPENPAR_TK:
		print("Expected ( at line,",line)
		exit(0)
	token,word=lex()
	actualparlist()

	if token!=CLOSEPAR_TK:
		print("expected ) at line", line)
		exit(0)
	token,word=lex()

def actualparlist():
	global token
	global word
	if token!=CLOSEPAR_TK:
		actualparitem()
		while token==COMMA_TK:
			token,word=lex()
			actualparitem()
	else:
		return

def actualparitem():
	global token
	global word
	EPlace=""
	if token==IN_TK:
		token,word=lex()
		EPlace=expression()
		genQuad("par",EPlace,"CV","_")
	elif token==INOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
		genQuad("par",word,"REF","_")
		token,word=lex()
	elif token==INANDOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
		genQuad("par",word,"RET","_")
		token,word=lex()
	else:
		print("error actual par item",line)
		exit(0)

def condition():
	global token
	global word
	BTrue=emptyList()
	BFalse=emptyList()
	Q1True=emptyList()
	Q1False=emptyList()
	Q2True=emptyList()
	Q2False=emptyList()

	Q1True,Q1False=boolterm()
	BTrue=Q1True
	BFalse=Q1False

	while token==OR_TK:
		backpatch(BFalse,nextQuad())
		token,word=lex()

		Q2True,Q2False=boolterm()
		BTrue=mergeList(BTrue,Q2True)
		BFalse=Q2False
	return BTrue,BFalse

def boolterm():
	global token
	global word
	QTrue=emptyList()
	QFalse=emptyList()
	R1True=emptyList()
	R1False=emptyList()
	R2True=emptyList()
	R2False=emptyList()

	R1True,R1False=boolfactor()

	QTrue=R1True
	QFalse=R1False

	while token==AND_TK:
		backpatch(QTrue,nextQuad())
		token,word=lex()
		R2True,R2False=boolfactor()

		QFalse=mergeList(QFalse,R2False)
		QTrue=R2True
	return QTrue,QFalse

def boolfactor():
	global token
	global word
	E1Place=""
	E2Place=""
	RTrue=emptyList()
	RFalse=emptyList()
	if token==NOT_TK:
		token,word=lex()
		if token==OPENBRACKET_TK:
			token,word=lex()
			RTrue,RFalse=condition()

		else:
			print("expected [ at line",line)
			exit(0)

		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
			exit(0)
		token,word=lex()

	elif token==OPENBRACKET_TK:
		token,word=lex()
		RTrue,RFalse=condition()

		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
			exit(0)
		token,word=lex()
	else:
		E1Place=expression()
		operator=word
		relational_oper()

		E2Place=expression()

		RTrue=makeList(nextQuad())
		genQuad(operator,E1Place,E2Place,"_")

		RFalse=makeList(nextQuad())
		genQuad("jump","_","_","_")

	return RTrue,RFalse

def expression():
	global token
	global word
	T1Place=""
	T2Place=""
	Eplace=""
	optional_sign()
	T1Place=term()

	while(token==PLUS_TK or token==MINUS_TK):
		operator=word
		add_oper()
		T2Place=term()
		t= newTemp()
		genQuad(operator,T1Place,T2Place,t)
		T1Place=t
	Eplace=T1Place

	return Eplace

def term():
	global token
	global word
	F1Place=""
	F2Place=""
	Tplace=""
	F1Place=factor()
	while(token==STAR_TK or token==SLASH_TK):
		operator=word
		mul_oper()
		F2Place=factor()
		t=newTemp()
		genQuad(operator,F1Place,F2Place,t)
		F1Place=t
	Tplace=F1Place
	return Tplace

def factor():
	global token
	global word
	Fplace = ""
	if token==DIGIT_TK:
		Fplace = word
		token,word=lex()
	elif token==OPENPAR_TK:
		token,word=lex()
		Fplace=expression()

		if token!=CLOSEPAR_TK:
			print("expected ) at line", line)
			exit(0)
		token,word=lex()
	elif token==ID_TK:
		Fplace= word
		token,word=lex()
		if token==OPENPAR_TK:
			idtail()
			t = newTemp()
			genQuad("par",t,"RET","_")
			genQuad("call", Fplace,"_","_")
			Fplace=t
	else:
		print("error in factor", line)
		exit(0)
	return Fplace

def idtail():
	global token
	global word
	if token==OPENPAR_TK:
		actualpars()
	else:
		return

def relational_oper():
	global token
	global word
	if token==EQUAL_TK:
		token,word=lex()
		return
	if token==LESSOREQUAL_TK:
		token,word=lex()
		return
	if token==GREATEROREQUAL_TK:
		token,word=lex()
		return
	if token==LESS_TK:
		token,word=lex()
		return
	if token==GREATER_TK:
		token,word=lex()
		return
	if token==DIF_TK:
		token,word=lex()
		return
	else:
		print("expected = <= >= <> < > at line", line)
		exit(0)

def add_oper():
	global token
	global word
	if token==PLUS_TK:
		token,word=lex()
		return
	if token==MINUS_TK:
		token,word=lex()
		return
	else:
		print("expected, + or - ", line)
		exit(0)

def mul_oper():
	global token
	global word
	if token==STAR_TK:
		token,word=lex()
		return
	if token==SLASH_TK:
		token,word=lex()
		return
	else:
		print("expected * or /", line)

def optional_sign():
	global token
	global word
	if token==PLUS_TK or token==MINUS_TK:
		add_oper()
	else:
		return

def intermediate_code(FileName):
	global intermediate
	FileName_new = FileName[:len(FileName)-3] + "int"
	output= open(FileName_new,"w")

	for i in range(len(intermediate)):
		interm=intermediate[i]
		code="" + interm[0] + ":" + interm[1] + " " + interm[2] + " " + interm[3] + " " + interm[4] + "\n"
		output.write(code)
	output.close()

def C_code(FileName):
	global intermediate
	FileName_new = FileName[:len(FileName)-3] + "c"
	f = open(FileName_new,"w")
	code = "int main(){ \n " + ",".join(variables)+ "\n"
	f.write(code)
	for i in range(len(intermediate)):
		interm = intermediate[i]
		code = interm[0]+" :"+" "

		if interm[1]==":=":
			code = code + interm[4]+"="+interm[2]
		if interm[1]=="+" or interm[1]=="-" or interm[1]=="*" or interm[1]=="/":
			code = code + interm[4]+"="+interm[2]+interm[1]+interm[3]
		if interm[1]=='<' or interm[1]=='>' or interm[1]=='<=' or interm[1]=='>=' or interm[1]=='<>':
			code = code + "if("+interm[2]+interm[1]+interm[3]+") goto "+interm[4]
		if interm[1]=='jump' :
			code = code + "goto "+interm[4]
		code = code + '\n'

		f.write(code)

	f.write("}; \n")
	f.close()

def add_scope():
	global symboltable
	global currentdepth

	Scope = scope()
	#Scope.offset = 12
	if len(symboltable)==0:
		scope.nestingLevel = 0
		currentdepth = 0
		Scope.offset = 12
	else:
		scope.nestingLevel = 1 + symboltable[len(symboltable)-2].nestingLevel
		currentdepth = currentdepth + 1
		Scope.offset = 12 + symboltable[len(symboltable)-2].offset

	symboltable = symboltable+[Scope]



def delete_scope():
	global symboltable
	global currentdepth
	current=currentdepth-1
	if len(symboltable)>1:

		scope = symboltable[current]
		Entity = scope.Entities[len(scope.Entities)-1]
		Entity.framelength = symboltable[current].baseoffset

	for Scope in symboltable:
		print (Scope.nestingLevel)
		for Entity in Scope.Entities:

			if Entity.entType==ID_TK:
				print ("\t",Entity.name,Entity.entType,Entity.offset)
			if Entity.entType==INOUT_TK or Entity.entType == INANDOUT_TK or Entity.entType == IN_TK:
				print ("\t",entity.name,entity.entType,entity.offset,entity.parmode )

			else:
				print("\t",Entity.name,Entity.entType,Entity.startquad,Entity.framelength,entity.arguments)



	symboltable.pop()
	currentdepth = currentdepth - 1

def add_entity(name, tp,quad):
	global symboltable

	#Scope = symboltable [currentdepth]
	Entity = entity(name,tp)

	if tp == ID_TK:
		baseoffset=symboltable [currentdepth].baseOffset
		Entity.offset = baseoffset + 4
		symboltable [currentdepth].baseOffset=symboltable [currentdepth].baseOffset + 4
	if tp == FUNCTION_TK:
		Entity.startquad=quad
		Entity.framelength=12
	if tp == INOUT_TK or tp == INANDOUT_TK or tp == IN_TK:
		parmode = tp

	symboltable [currentdepth].Entities.append(Entity)

def add_argument(par):
	global symboltable

	Argument = argument(par)

	symboltable[currentdepth].Entities[len(Entities)-1].arguments.append(Argument)

def Search_Entity(n):
	global symboltable

	for Scope in symboltable:
		for Entity in Scope.Entities:
			if Entity.name == n:

				return Scope.nestingLevel, Entity.entType, Entity.offset, Entity.startquad, Entity.arguments ,Entity.framelength, Entity.value, Entity.parMode

	#			if Entity.entType==ID_TK:
	#				return Scope.nestingLevel,Entity.name,Entity.entType,Entity.offset

	#			if Entity.entType==INOUT_TK or Entity.entType == INANDOUT_TK or Entity.entType == IN_TK:
	#				return Scope.nestingLevel,Entity.name,Entity.entType,Entity.offset,Entity.parmode

	#			else:
	#				return Scope.nestingLevel,Entity.name,Entity.entType,Entity.startquad,Entity.framelength,Entity.arguments

def gnvlcode(a):
	global symboltable
	global currentdepth
	global finalcode

	level,type,offset,startquad,arguments,framelength,value,parmode=Search_Entity(a)
	code = ''
	code = code+"lw $t0,-4($sp) \n"
	for i in range(level):
		code = code+"lw $t0,-4($t0) \n"
	code = code + "add $t0, $t0, -"+offset+"\n"
	finalcode = finalcode + [code]

def loadvr(v,r):
#	global r
#	r = 0 
	global symboltable
	global currentdepth
	global finalcode
	code = ''
	level,type,offset,startquad,arguments,framelength,value,parmode=Search_Entity(v)
	if type=="constant":
		code = code + "li $t"+str(r)+","+str(v)+'\n'
		r = r + 1
	elif level==0:
		code = code + "lw $t"+str(r)+",-"+offset+"($fp)\n"
		r = r + 1 
	elif type == "variable" or parmode == "CV" and level==currentdepth:
		code = code + "lw $t"+str(r)+",-"+offset+"($fp)\n"
	elif type == "variable" or parmode == "CV" and level==currentdepth:
		code = code + "lw $t"+str(r)+",-"+offset+"($fp)\n"
		r = r + 1
	elif parmode == "REF":
		code = code + "$t0,-"+offset+"($sp)\n"
		code = code + "$t"+str(r)+",($t0)\n"
		r = r + 1 
		finalcode = finalcode + [code]
	elif type== "variable" or parmode== "CV" and level<currentdepth :
		gnvlcode(v)
		code = code +  "lw $t"+str(r)+",($t0)\n"
		r = r + 1
	elif level<currentdepth and parmode=="REF":
		gnvlcode(v)
		code = code + "lw $t0,($t0)\n"
		code = code + "$t"+str(r)+",($t0)"
		r = r + 1
	finalcode = finalcode + [code]
	
		
def storevr(v,r):
	global symboltable
	global currentdepth
	global finalcode
	code = ''
	level,type,offset,startquad,arguments,framelength,value,parmode=Search_Entity(v)
	if level == 0:
		code = code + "sw $t"+str(r)+",-"+offset+"($s0)\n"
		r = r + 1
	elif type == "variable" and currentdepth == level or parmode==IN_TK:
		code = code + "sw $t"+str(r)+"-"+offset+"($sp)\n"
		r = r + 1
	elif parmode == INANDOUT_TK and currentdepth== level:
		code = code + "lw $t0,-"+offset+"($sp)\n"
		code = code + "sw $t"+str(r)+",($t0)\n"
		r = r + 1
	elif currentdepth > level and type == "variable" or parmode == IN_TK:
		gnvlcode(v)
		code = code + "sw $t"+str(r)+",($t0)\n"
		r = r + 1 
	elif parmode == INANDOUT_TK:
		gnvlcode(v)
		code = code + "lw $t0, ($t0)\n"
		code = code + "sw $t"+str(r)+",($t0)\n"
		r = r + 1
	finalcode = finalcode + [code]						   

f=open(sys.argv[1],"r")
program()
intermediate_code(sys.argv[1])
C_code(sys.argv[1])
