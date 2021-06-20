""" AUTOR: Gabriel Lamarão da Silva Costa """
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
    mapa_karnaugh = {}
    combinacao = ''

    for m in range(0, len(lista_convertida)):
        print('\nSaida da Tabela verdade não simplificada:')
        saidaDaTabela = []
        tabelaVerdade = []
        saidaDaTabela = lista_convertida[m]
        tamanhoDaSaida = len(saidaDaTabela)
        qtdEntradas = calculaEntradas(tamanhoDaSaida)
        print(qtdEntradas)
        insereEntradas(tabelaVerdade, qtdEntradas, tamanhoDaSaida)
        for i in range(0, tamanhoDaSaida):
            if(saidaDaTabela[i]==1):
                for coluna in range(0, qtdEntradas):
                    for linha in range(0, tamanhoDaSaida):
                        if(linha==i):
                            if(tabelaVerdade[coluna][linha]==0):
                                print("{}'".format(valoresEntradas[coluna]), end='')
                            else:
                                print("{}".format(valoresEntradas[coluna]), end='')
                            if(coluna==qtdEntradas-1):
                                if(coluna==qtdEntradas):
                                    continue
                                print(' +', end=' ')
        print(' ')
        print('\nMapa de Karnaugh:')
        for linhaSaida in range(0, pow(2, qtdEntradas)):
            if saidaDaTabela[linhaSaida] == 0:
                for coluna in range(0, qtdEntradas):
                    for linha in range(0, linhaSaida + 1):
                        if linha == linhaSaida:
                            if combinacao == '':
                                combinacao = str(tabelaVerdade[coluna][linha])
                            else:
                                combinacao += str(tabelaVerdade[coluna][linha])
                                if len(combinacao) == qtdEntradas:
                                    mapa_karnaugh[combinacao] = 0
                                    combinacao = ''

            if saidaDaTabela[linhaSaida] == 1:
                for coluna in range(0, qtdEntradas):
                    for linha in range(0, linhaSaida + 1):
                        if linha == linhaSaida:
                            if combinacao == '':
                                combinacao = str(tabelaVerdade[coluna][linha])
                            else:
                                combinacao += str(tabelaVerdade[coluna][linha])
                                if len(combinacao) == qtdEntradas:
                                    mapa_karnaugh[combinacao] = 1
                                    combinacao = ''

        if qtdEntradas == 2:
            print('{} {}'.format(mapa_karnaugh['00'], mapa_karnaugh['01']))
            print('{} {}'.format(mapa_karnaugh['10'], mapa_karnaugh['11']))

        if qtdEntradas == 3:
            print('{} {} {} {}'.format(mapa_karnaugh['000'], mapa_karnaugh['001'], mapa_karnaugh['011'],
                                       mapa_karnaugh['010']))
            print('{} {} {} {}'.format(mapa_karnaugh['100'], mapa_karnaugh['101'], mapa_karnaugh['111'],
                                       mapa_karnaugh['110']))
        if qtdEntradas == 4:
            print('{} {} {} {}'.format(mapa_karnaugh['0000'], mapa_karnaugh['0001'],
                                       mapa_karnaugh['0011'], mapa_karnaugh['0010']))
            print('{} {} {} {}'.format(mapa_karnaugh['0100'], mapa_karnaugh['0101'],
                                       mapa_karnaugh['0111'], mapa_karnaugh['0110']))
            print('{} {} {} {}'.format(mapa_karnaugh['1000'], mapa_karnaugh['1001'],
                                       mapa_karnaugh['1011'], mapa_karnaugh['1010']))
            print('{} {} {} {}'.format(mapa_karnaugh['1100'], mapa_karnaugh['1101'],
                                       mapa_karnaugh['1111'], mapa_karnaugh['1110']))



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

caminhoDoArquivo = '/home/gabriel/PycharmProjects/Eletronica/binarios.txt'
lista = leArquivo(caminhoDoArquivo)
print(lista)
calculaSaida(lista)
