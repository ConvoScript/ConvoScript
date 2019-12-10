import ply.yacc as yacc
import ConvoIntermediate
 
# Get the token map from the lexer.  This is required.
from ConvoLexer import tokens

def p_function_open(p):
    '''
    function : OPEN LPAREN RPAREN
    '''
    ConvoIntermediate.openCommunication(p[3])
    print(p[3])

def p_function_close(p):
    '''
    function : CLOSE LPAREN RPAREN
    '''
    print(p[1])

def p_function_join(p):
    '''
    function : JOIN LPAREN IP RPAREN
    '''
    print(p[1])
    # ConvoIntermediate.joinComm(p,'127.0.0.1')
    ConvoIntermediate.joinCommunication(p[3])

def p_function_send(p):
    '''
    function : SEND LPAREN data RPAREN
    '''
    print(p[1])
    ConvoIntermediate.sendData(p_data())


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
        #s = raw_input('ConvoScript > ')
        s = input('ConvoScript > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)