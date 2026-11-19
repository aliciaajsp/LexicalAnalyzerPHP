import ply.lex as lex

tokens = [
    'PHP_OPEN',
    'PHP_CLOSE',
    'PRINT',
    'ECHO',
    'STRING',
    'SEMICOLON'
]

t_PHP_OPEN = r'<\?php'
t_PHP_CLOSE = r'\?>'

t_SEMICOLON = r';'

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t

def t_PRINT(t):
    r'PRINT'
    return t

def t_ECHO(t):
    r'ECHO'
    return t

def t_comment(t):
    r'//[^\n]*'
    pass

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = r'''
<?php //php 7.2.24

PRINT "Hello, world! \n";
ECHO "Welcome "

?>
'''

if __name__ == '__main__':

    lexer.lineno = 1
    lexer.input(data)

    print("\n===== SIMPLE STATEMENT LEXICAL ANALYSIS =====\n")

    while True:
        tok = lexer.token()

        if not tok:
            break

        print(f"{tok.type:<12} -> {tok.value}")

    print("\n===== END OF ANALYSIS =====")