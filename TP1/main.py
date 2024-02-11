

def main():
    file = open('emd.csv', 'r')
    data = file.read()
    linhas = data.split('\n')

    linhas = linhas[1:-1]
    escalao = {'[20,24]': 0, '[25,29]': 0, '[30,34]': 0, '[35,39]': 0}

    modalidades = set()
    apto = 0
    inapto = 0

    for linha in linhas:
        campos = linha.split(',')
        modalidades.add(campos[8])

        if campos[12] == "true":  # aptidao
            apto += 1
        else:
            inapto += 1

        idade = int(campos[5])

        if 20 <= idade <= 24:
            escalao['[20,24]'] += 1
        elif 25 <= idade <= 29:
            escalao['[25,29]'] += 1
        elif 30 <= idade <= 34:
            escalao['[30,34]'] += 1
        elif 35 <= idade <= 39:
            escalao['[35,39]'] += 1

    list_mod = list(modalidades)
    list_mod.sort()
    perc_apto = (apto / (apto+inapto)) * 100
    perc_inapto = (inapto / (apto+inapto)) * 100

    print(list_mod)
    print(f"{perc_apto} % dos atletas estao aptos")
    print(f"{perc_inapto} % dos atletas estao inaptos")
    print(escalao)


if __name__ == "__main__":
    main()

