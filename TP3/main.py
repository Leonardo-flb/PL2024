import re, sys

acc = 0

digitos = r'(\d+)'
on = r'(?i:on)'
off = r'(?i:off)'
igual = r'\='

ler = False

file=sys.stdin.read()
palavras = re.findall(r'\w+|=',file)
for palavra in palavras:
    if re.search(on, palavra):
        ler = True
        print(palavra)
    if re.search(off, palavra):
        ler = False
    if re.search(digitos, palavra):
        print(palavra)
        if ler:
            acc += int (re.search(digitos, palavra).group(1))
    if re.search(igual,palavra):
        print(f"SOMA: {acc}")

