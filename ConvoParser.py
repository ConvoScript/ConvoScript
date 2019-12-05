import ply.yacc as yacc
import ConvoIntermediate
 
# Get the token map from the lexer.  This is required.
from ConvoLexer import tokens

def p_function_open(p):
    '''
    function : OPEN LPAREN IP RPAREN
    '''
    ConvoIntermediate.printer()
    print(p[3])

def p_function_close(p):
    '''
    function : CLOSE LPAREN RPAREN
    '''
    print(p[1])

def p_function_ping(p):
    '''
    function : PING LPAREN RPAREN
             | PING LPAREN IP RPAREN
    '''
    print(p[1])

def p_function_send(p):
    '''
    function : SEND LPAREN data RPAREN
    '''
    print(p[1])

def p_data(p):
    '''
    data : STRING
         | WORD
         | INTEGER
    '''
    print(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('ConvoScript > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)