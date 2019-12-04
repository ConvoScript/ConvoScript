import ply.lex as lex
import sys
tokens = [
    'COMMA',
    'LPAR',
    'RPAR',
    'NUMBER',
    'STRING',
]
reserved = {
     'Open': 'OPEN',
     'Close':'CLOSE',
     'Send': 'SEND',
     'Receive': 'RECEIVE',
     'Ping': 'PING',

}

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_STRING  = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA = r','

