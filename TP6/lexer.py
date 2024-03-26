import ply.lex as lex
import sys,re 

## ? a
## b - a * 2 / (27 - 3) 
## ! a + b
## c = a * b

tokens = (
    "INTERROGACAO",
    "EXCLAMACAO",
    "NUM",
    "MINUS",
    "PLUS",
    "TIMES",
    "DIVIDE",
    "EQUALS",
    "ID",
    "PA",
    "PF"
)

t_INTERROGACAO = r'\?'
t_EXCLAMACAO = r'\!'
t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_PA = r'\('
t_PF = r'\)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]\w*'
    return t 

# Regra para lidar com espaços em branco
t_ignore = ' \t'

# Função para lidar com quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função para lidar com erros
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

def t_eof(t):
    r'\$'
    t.value = None
    return t

lexer = lex.lex()

data = """
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b
"""
lexer.input(data)

while True:
    token = lexer.token()
    if token.type == "eof":
        break
    print(token)