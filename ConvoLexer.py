# An implentation of Dartmouth BASIC (1964)

import ply.lex as lex

keywords = (
    'OPEN', 'CLOSE', 'JOIN', 'SEND', 'RECEIVE',
)

tokens = keywords + (
    'EQUALS', 'LPAREN', 'RPAREN', 'COMMA', 
    'SEMI', 'IP', 'INTEGER', 'STRING',
    'WORD', 'NEWLINE',
)

t_ignore = ' \t'


def t_REM(t):
    r'REM .*'
    return t


def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t

t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_IP = r'\d+\.\d+\.\d+\.\d+'
t_STRING = r'\".*?\"'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)

# Build the lexer
lexer = lex.lex()
