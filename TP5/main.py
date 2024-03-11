import re

ingredientes = [
    ("1","Barrinha de Granola", 2.50),
    ("2","Água Mineral", 1.00),
    ("3","Sanduíche de Frango", 3.50),
    ("4","Salada de Frutas", 2.00),
    ("5","Batatas Chips", 1.50),
    ("6","Iogurte com Frutas", 2.75),
    ("7","Chocolate", 1.75),
    ("8","Café Expresso", 1.50),
    ("9","Maçã", 1.25),
    ("10","Sopa Instantânea", 2.25),]

moedas = {r'2e':2.00,
          r'1e':1.00,
          r'50c':0.50,
          r'20c':0.20,
          r'10c': 0.10,
          r'5c':0.05
          }


# Regular expressions

listar = r'[Ll][Ii][Ss][Tt][Aa][Rr]'
money = r'[Mm][Oo][Ee][Dd][Aa]' # ([125]0?[ec]\,\s?)*[125]0?[ec]$
moeda = r'[125]0[c]|[12]e'

selecionar = r'(?i:selecionar) (\d+)'
sair = r'(?i:sair)'

def lista(): 
    print(f"\n-------------------------------")
    for (n,nome,preco) in ingredientes:
        if (int(n)/10 < 1):
            print(f"0{n} | {nome} | {preco}")
        else:
            print(f"{n} | {nome} | {preco}")
    print(f"-------------------------------\n")

def dinheiro(lista):   
    soma = 0 
    for moeda in lista:
        soma += moedas[moeda]
    return soma

def select(opcao ,saldo):
    for n, nome, preco in ingredientes:
        if opcao == n : 
            if saldo < preco:
                return -1
            else:
                saldo -= preco
                return saldo , nome
    return -2



def __main__():
    saldo = 0.00 
    while True:
        exp = input("O que deseja fazer: ")
        if re.search(listar,exp):
            lista()

        elif re.search(money,exp):
            l_moedas=re.findall(moeda,exp)
            saldo += dinheiro(l_moedas)
            if saldo > 0:
                print(f"Saldo : {round(saldo,2)} €")
            else:
                print("Input incorreto")
        
        elif re.search(selecionar,exp):
            opcao = re.search(selecionar,exp).group(1)
            res , nome = select(opcao,saldo)
            if res > 0 :
                saldo = res
                print(f"Saldo : {round(saldo,2)} €\nEntregue: {nome}")
            elif res == -1:
                print(f"\nSaldo insuficiente para esse produto!\n")
            else:
                print("\nProduto indisponivel!\n")

        elif re.search(sair,exp):
            print(f"Troco: {round(saldo,2)} €\nObrigado pela sua preferência :)")
            break


if __name__ == "__main__":
    __main__()

