import ply.lex as lex

# expressoes reservadas
reservadas = {
    'Select': 'Select',
    'From': 'From',
    'Where': 'Where'
}

# Lista de tokens
tokens = list(reservadas.values()) + [ 
    'Id',
    'Numero',
    'Virgula',
    'Maior_igual',
    'Menor_igual',
    'Igual'
]

# Regras de expressões regulares para os tokens
t_Select = r'(?i:select)'
t_From = r'(?i:from)'
t_Where = r'(?i:where)'
# t_Id = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_Numero = r'\d+'
t_Virgula = r','
t_Maior_igual = r'>='
t_Menor_igual = r'<='
t_Igual = r'='

# Regra para lidar com espaços em branco
t_ignore = ' \t'

# Função para lidar com quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_Id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'Id') 
    return t
# Função para lidar com erros
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)



# Construção do lexer
lexer = lex.lex()

# Exemplo do enunciado 
query = "Select id, nome, salario From empregados Where salario >= 820"
query2 = "Select nome, salario From empregados Where salario >= 1000 AND departamento = 'Vendas'"
query3 = "Select id, nome, cidade From clientes"
lexer.input(query3)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
