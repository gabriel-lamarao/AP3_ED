
def calculaEntradas (tamanhoDaSaida):
    contadorEntradas = 0
    while tamanhoDaSaida != 1:
        tamanhoDaSaida = tamanhoDaSaida / 2
        contadorEntradas += 1
    return contadorEntradas

def insereEntradas(tabelaVerdade, qtdEntradas, tamanhoDaSaida):
    for i in range(0, qtdEntradas):
        linha = []
        tamanhoDaSaida = int(tamanhoDaSaida / 2)
        while len(linha) < pow(2, qtdEntradas):
            for j in range(0, tamanhoDaSaida):
                linha.append(0)
            for h in range(0, tamanhoDaSaida):
                linha.append(1)
        tabelaVerdade.append(linha)

def calculaSaida(lista_convertida):
    valoresEntradas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I,' 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    for m in range(0, len(lista_convertida)):
        numerosDeSaida = []
        tabelaVerdade = []
        numerosDeSaida = lista_convertida[m]
        tamanhoDaSaida = len(numerosDeSaida)
        qtdEntradas = calculaEntradas(tamanhoDaSaida)
        insereEntradas(tabelaVerdade, qtdEntradas, tamanhoDaSaida)
        for i in range(0, tamanhoDaSaida):
            if(numerosDeSaida[i]==1):
                for coluna in range(0, qtdEntradas):
                    for linha in range(0, tamanhoDaSaida):
                        if(linha==i):
                            if(tabelaVerdade[coluna][linha]==0):
                                print("{}'".format(valoresEntradas[coluna]), end='')
                            else:
                                print("{}".format(valoresEntradas[coluna]), end='')
                            if(coluna==qtdEntradas-1):
                                print(' +', end=' ')
        print(' ')

def leArquivo(caminhoDoArquivo):
    arquivo = open(caminhoDoArquivo)
    linha = str(arquivo.read())
    linha = linha.split('\n')
    lista_separada = []
    lista_convertida = []
    for i in range(0, len(linha)):
        lista_separada.append(linha[i].split(' '))
    for j in range(0, len(lista_separada)-1):
        entrada_atual = []
        for k in range(0, len(lista_separada[j])):
            numero_atual = lista_separada[j][k]
            numero_atual = int(numero_atual)
            entrada_atual.append(numero_atual)
        lista_convertida.append(entrada_atual)
    return lista_convertida

    '''linha = linha.replace('\n', '')
    linha = linha.split(' ')
    linha = [int(g) for g in linha]
    print(linha)
    tamanhoDaSaida = len(linha)
    qtdEntradas = calculaEntradas(tamanhoDaSaida)
    tabelaVerdade = []
    insereEntradas(tabelaVerdade, qtdEntradas, tamanhoDaSaida)
    print(tabelaVerdade)
    calculaSaida(linha, tamanhoDaSaida, qtdEntradas, tabelaVerdade)'''


caminhoDoArquivo = '/home/gabriel/PycharmProjects/Eletronica/binarios.txt'
lista = leArquivo(caminhoDoArquivo)
calculaSaida(lista)
