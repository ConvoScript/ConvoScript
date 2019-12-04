import ply.lex as lex
import sys
tokens = [
    'COMMA',
    'LPAR',
    'RPAR',
    'NUMBER',
    'STRING',
    'EQUALS',
]
reserved = {
     'Open': 'OPEN',
     'Close':'CLOSE',
     'Send': 'SEND',
     'Receive': 'RECEIVE',
     'Ping': 'PING',
}

# Regular expression rules for simple tokens
t_COMMA = r'\,'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_EQUALS  = r'\='
def t_NUMBER(t):
    r'(\d+)'
    return t

def t_STRING(t):
    r'\"[a-zA-Z0-9_?!@#$%&*-+().~, \t\n]*\"'
    return t

def t_newline(self,t):
         r'\n+'
         t.lexer.lineno += len(t.value)

#Build Lexer
lexer = lex.lex()



