import ply.lex as lex

# LIST OF TOKENS
tokens = [
    'PHP_OPEN',
    'PHP_CLOSE',
    'PRINT',
    'IF',
    'ELSE',
    'VARIABLE',
    'NUMBER',
    'STRING',
    'ASSIGN',
    'CONCAT',
    'GT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON'
]

# TOKEN RULES

# PHP tags
t_PHP_OPEN = r'<\?php'
t_PHP_CLOSE = r'\?>'

# Operators
t_ASSIGN = r'='
t_CONCAT = r'\.'
t_GT = r'>'

# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# VARIABLE TOKEN
def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# NUMBER TOKEN
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# STRING TOKEN
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t

# KEYWORD TOKENS
def t_PRINT(t):
    r'PRINT'
    return t

def t_IF(t):
    r'IF'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

# IGNORE SPACES AND TABS
t_ignore = ' \t'

# TRACK LINE NUMBERS
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ERROR HANDLING
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

# BUILD THE LEXER
lexer = lex.lex()