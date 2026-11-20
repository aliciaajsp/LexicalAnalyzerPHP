import ply.lex as lex

tokens = [
    'PHP_OPEN',
    'PHP_CLOSE',
    'PRINT',
    'ECHO',
    'IF',
    'ELSE',
    'WHILE',
    'VARIABLE',
    'NUMBER',
    'STRING',
    'ASSIGN',
    'PLUS',
    'DIVIDE',
    'MOD',
    'CONCAT',
    'GT',
    'NE',
    'LE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON'
]


t_PHP_OPEN = r'<\?php'
t_PHP_CLOSE = r'\?>'


t_ASSIGN = r'='
t_PLUS = r'\+'
t_DIVIDE = r'/'
t_MOD = r'%'
t_CONCAT = r'\.'
t_GT = r'>'
t_NE = r'!='
t_LE = r'<='


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'


def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t


def t_PRINT(t):
    r'print'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
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
