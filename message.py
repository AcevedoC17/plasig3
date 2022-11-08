def p_main(p):
    'main : INT INT ARROW INT'
    p[0]=[[p[1],p[2]],'=>',p[2]]


def p_defdefs(p):
    '''defdefs : defdef defdefs
              | defdef'''
    if len(p)==2:
        p[1].append(p[2])
        p[0]=p[1]
    else:
        p[0]=p[1]
    pass

def p_defdef(p):
    'defdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE'
    if type(p[7])!=type(p[12]):
        print("Error in types")
    else:
        p[0]=[p[1],p[2],p[4],p[7],'=',p[10],p[11],p[12]]
    pass

def p_parmsopt(p):
    '''parmsopt : parms
                | empty'''
    p[0]=p[1]
    pass

def p_parms(p):
    '''parms : vardef COMMA parms
            | vardef'''
    if len(p)==4:
        p[0]=[p[0]]+p[3]
    else:
        p[0]=p[1]
    pass

def p_vardef(p):
    'vardef : ID COLON type'
    p[0]=[p[1],p[2]]
    pass

def p_type(p):
    '''type : INT
            | LPAREN typesopt RPAREN ARROW type'''
    if(len(p)==2):
        p[0]=p[1]
    else:
        p[0]=[p[1],'=>',p[5]]
    pass

def p_typesopt(p):
    '''typesopt : types
                | empty'''
    p[0]=p[1]
    pass 

def p_types(p):
    '''types : type COMMA types
            | type'''
    if len(p)==4:
        p[0]=[p[1]]+p[3]
    else:
        p[0]=p[1]
    pass

def p_vardefsopt(p):
    '''vardefsopt : VAR vardef SEMI vardefsopt
                  | empty'''
    if(len(p)==5):
        p[0]=[[p[1],p[2]]]+p[4]
    else:
        p[0]=p[1]
    pass

def p_defdefsopt(p):
    '''defdefsopt : defdefs
                  | empty'''
    p[0]=p[1]
    pass

def p_expras(p):
    '''expras : expra SEMI expras
              | expra'''
    if(len(p)==4):
        p[0]=[p[0]]+p[3]
    else:
        p[0]=[p[1]]
    pass

def p_expra(p):
    '''expra : ID BECOMES expr
            | expr'''
    if(len(p)==4):
        if type(p[1])!=type(p[3]):
            print("Error in types")
        else:
            p[1]=p[3]#Standby
    else:
        p[0]=p[1]
    pass

def p_expr(p):
    '''expr : IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE
            | term
            | expr PLUS term
            | expr MINUS term'''
    if (len(p)==12):
        if type(p[6])!=type(p[10]):
            print("Error in types")
        else:
            if(p[3]):
                p[6]
            else:
                p[10]
    elif(len(p)==2):
        p[0]=p[1]
    elif(len(p)==4):
        if not isinstance(p[1], int) and not isinstance(p[3], int):
            print("Types must be Int")
        else:
            if p[2]=='+':
                p[0]=p[1]+p[3]
            elif p[2]=='-':
                    p[0]=p[1]-p[3]
    pass

def p_term(p):
    '''term : factor
            | term STAR factor
            | term SLASH factor
            | term  PCT factor'''
    if(len(p)==2):
        p[0]=p[1]
    elif(len(p)==4):
        if type(p[1]) !='int' and type(p[3])!='int':
            print("Types must be Int")
        else:
            if p[2]=='*':
                p[0]=p[1]*p[3]
            elif p[2]=='/':
                p[0]=p[1]/p[3]
            elif p[2]=='%':
                p[0]=p[1]%p[3]
        
    pass

def p_factor(p):
    '''factor : ID
              | NUM
              | LPAREN expr RPAREN
              | factor LPAREN argsopt RPAREN'''
    if(len(p)==2):
        if type(p[0])!=type(p[1]):
            print("Error in types")
        else:
            if p[1]=='ID':
                p[0]=['id',p[1]]
            else:
                p[0]=p[1]
    elif(len(p)==4):
        p[0]=p[2]
    elif(len(p)==5):
        p[0]=[p[1],p[0]]
    pass

def p_test(p):
    '''test : expr NE expr
            | expr LT expr
            | expr LE expr
            | expr GE expr
            | expr GT expr
            | expr EQ expr'''
    if p[2]=='!=':
        p[0]=p[1]!=p[3]
    elif p[2]=='<':
        p[0]=p[1]<p[3]
    elif p[2]=='<=':
        p[0]=p[1]<=p[3]
    elif p[2]=='>=':
        p[0]=p[1]>=p[3]
    elif p[2]=='>':
        p[0]=p[1]>p[3]
    elif p[2]=='==':
        p[0]=p[1]==p[3]
    pass

def p_argsopt(p):
    '''argsopt : args
              | empty'''
    p[0]=p[1]
    pass

def p_args(p):
    '''args : expr COMMA args
            | expr'''
    if(len(p)==4):
        p[0]=[p[0]]+p[3]
    else:
        p[0]=p[1]
    pass

def p_error(p):
    print("Syntax error in input: " + str(p))
    pass
 
def p_empty(p):
    'empty :'
    p[0]=None
    pass
