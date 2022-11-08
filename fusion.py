
import ply.lex as lex
import ply.yacc as yacc


# Carlos A. Acevedo Morales
# 802-19-0977
# 10-10-2022
# CIIC4030-066

#textfile = open("test.txt", 'r', errors='ignore').read()


text = "def f(a:Int, b:Int):Int = { var c:Int; def g(a:Int, b:(Int)=>Int):Int = { b(a) }def h(c:Int):Int = { def g():Int = { c-b } g() } c = a+b; g(c,h) }"
# tokens = (
#     'ID', # a string consisting of any letter (a-z or A-Z) followed by zero or more letters and digits (0-9), but not equal to any of the keywords def,var,int,if,else.
#     'DEF',
#     'VAR',
#     'INT',
#     'IF',
#     'ELSE',
#     'NUM',
#     'LPAREN',
#     'RPAREN',
#     'LBRACE',
#     'RBRACE',
#     'BECOMES',
#     'EQ',
#     'NE', 
#     'LT', 
#     'GT', 
#     'LE',
#     'GE', 
#     'PLUS', 
#     'MINUS',
#     'STAR',
#     'SLASH', 
#     'PCT', 
#     'COMMA', 
#     'SEMI',
#     'COLON',
#     'ARROW',
#     'COMMENT',
#     'WHITESPACE'
#     )

class Lexer(object):
  
    tokens = (
    'ID', # a string consisting of any letter (a-z or A-Z) followed by zero or more letters and digits (0-9), but not equal to any of the keywords def,var,int,if,else.
    'DEF',
    'VAR',
    'INT',
    'IF',
    'ELSE',
    'NUM',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'BECOMES',
    'EQ',
    'NE', 
    'LT', 
    'GT', 
    'LE',
    'GE', 
    'PLUS', 
    'MINUS',
    'STAR',
    'SLASH', 
    'PCT', 
    'COMMA', 
    'SEMI',
    'COLON',
    'ARROW',
    'COMMENT',
    'WHITESPACE'
    )

    # Token variables

    t_DEF = r'(def)'
    t_VAR = r'(var)'
    t_IF = r'(if)'
    t_ELSE = r'(else)'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_BECOMES = r'\='
    t_EQ = r'(==)'
    t_NE = r'(!=)'
    t_LT = r'\<'
    t_GT = r'\>'
    t_LE = r'(<=)'
    t_GE = r'(>=)'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_STAR = r'\*'
    t_SLASH = r'/'
    t_PCT = r'\%'
    t_COMMA = r'\,'
    t_SEMI = r'\;'
    t_COLON = r'\:'
    t_ARROW = r'(=>)'
    t_ignore_WHITESPACE = r'\s+'
    t_NUM = r'\d+'
    t_ignore_COMMENT = r'[/]{2}(.+)?'

    reserved = {
        'if' : 'IF',
        'def' : 'DEF',
        'var' : 'VAR',
        'else' : 'ELSE',
        'Int' : 'INT'
    }


    def t_INT(self,t):
        r'\d+'
        t.value = int(t.value)
        return t



    def t_newline(self,t):
         r'\n+'
         t.lexer.lineno += len(t.value)



    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')
        return t

    def t_error(self,t):
         print("Illegal character '%s'" % t.value[0])
         t.lexer.skip(1)

    def build(self,**kwargs):
         self.lexer = lex.lex(module=self, **kwargs)


    def test(self,data):
         self.lexer.input(data)
         while True:
              tok = self.lexer.token()
              if not tok: 
                  break
              print(tok)



lexObj = Lexer()
lexObj.build()
tokens=lexObj.tokens

#############################################




start = "defdefs" 

def p_defdefs(p):
    '''defdefs : defdef defdefs
              | defdef'''
    if len(p)==3:
        p[0]=[p[1], p[2]]
    else:
        p[0]=p[1]
    pass

def p_defdef(p):
    'defdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE'
    if type(p[7])!=type(p[12]):
        print(" p_defdef violation : Error in types")
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
        p[0]=[p[0] , p[3]]
    else:
        p[0]=p[1]
    pass

def p_vardef(p):
    'vardef : ID COLON type'
    p[0]=p[3]
    pass

def p_type(p):
    '''type : INT
            | LPAREN typesopt RPAREN ARROW type'''
    if(len(p)==2):
        p[0]=p[1]
    else:
        p[0]=[p[2], p[5]]
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
        p[0]=[p[1], p[3]]
    else:
        p[0]=p[1]
    pass

def p_vardefsopt(p):
    '''vardefsopt : VAR vardef SEMI vardefsopt
                  | empty'''
    if(len(p)==5):
        p[0] = [p[2], p[4]]
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
        p[0]=[p[1], p[3]]
    else:
        p[0]=p[1]
    pass

def p_expra(p):
    '''expra : ID BECOMES expr
            | expr'''
    if(len(p)==4):
        if type(p[1])!=type(p[3]):
            print("p_expra : Error in types")
        else:
            p[0]=p[3]
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
            print("p_ expr: Error in types")
        else:
            p[0] = [p[3], p[6], p[10]]
    elif(len(p)==2): # 
        p[0]=p[1]
    elif(len(p)==4):
            if p[2] == '+':
                p[0] = [p[1], p[3]]
            elif p[2] =='-':
                    p[0] = [p[1], p[3]]
    pass 

def p_term(p):
    '''term : factor
            | term STAR factor
            | term SLASH factor
            | term  PCT factor'''
    if(len(p)==2):
        p[0] = p[1]
    if(len(p)==4):
        if type(p[1]) != type(p[3]):
            print("p_term : Types must be Int")
        else:
            if p[2]=='*':
                p[0] = p[1] *  p[3]
            elif p[2]=='/':
                p[0] = p[1] / p[3]
            elif p[2]=='%':
                p[0] = p[1] % p[3]
        
    pass

def p_factor(p):
    '''factor : ID
              | NUM
              | LPAREN expr RPAREN
              | factor LPAREN argsopt RPAREN'''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0]=p[2]
    elif(len(p)==5):
        p[0]=[p[1], p[3]]
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
        p[0]=[p[1] , p[3]]
    else:
        p[0]=p[1]
    pass

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        pass
    else:
        print("Syntax error at EOF")
 
def p_empty(p):
    'empty :'
    pass



if __name__ == "__main__":
     
     parser = yacc.yacc()
     analysis = "def f(a:Int, b:Int):Int = { var c:Int; def g(a:Int, b:(Int)=>Int):Int = { b(a) } } def h(c:Int):Int = { def g():Int = { c-b } g() } c = a+b; g(c,h) }"
     textfile = input()
     print(parser.parse(textfile))
