""" AUTOR: Gabriel Lamarão da Silva Costa
    Trabalho realizado com o auxílio do stackoverflow
"""
arquivo = open("/home/gabriel/Documentos/numeros.txt")
numeros = str(arquivo.read()).split()
numeros = [int(g) for g in numeros]


def print_zeros(binario):
    binario = binario[2:]
    tamanho = len(binario)
    completa_zeros = str("0" * (8 - tamanho))
    binario = str(binario)
    return completa_zeros + binario


def print_uns(binario):
    tamanho = len(binario)
    completa_zeros = str("1" * (8 - tamanho))
    binario = str(binario)
    return completa_zeros + binario


def complemento_a_1(binario):
    binario_invertido = ''
    if binario[1] == 'b':
        inverter_binario = binario[2:]
    else:
        inverter_binario = binario

    for i in inverter_binario:
        if i == '0':
            binario_invertido += '1'
        else:
            binario_invertido += '0'
    return binario_invertido


def complemento_a_2(binario):
    complemento_a_1(binario)
    um_binario = bin(1)
    compl_a_dois = -(int(binario, 2) + int(um_binario, 2))
    return compl_a_dois


def soma(lista):
    print("-" * 32, "SOMA", "-" * 33)
    for i in range(0, len(lista) - 1):
        if i / 2 % 1:
            continue
        a = lista[i]
        b = lista[i + 1]
        bin_a = bin(a)
        bin_b = bin(b)
        soma_inteiro = int(bin_a, 2) + int(bin_b, 2)
        soma_binario = bin(soma_inteiro)
        print(print_zeros(bin_a), "->", a, " + ", print_zeros(bin_b), "->", b, "=", print_zeros(soma_binario), "->",
              soma_inteiro)


def subtracao(lista):
    print("-" * 30, "SUBTRAÇÃO", "-" * 30)
    for i in range(0, len(lista) - 1):
        if i / 2 % 1:
            continue
        a = lista[i]
        b = lista[i + 1]
        if b > a:
            aux = b
            b = a
            a = aux
        bin_a = bin(a)
        bin_b = bin(b)
        subt_inteiro = int(bin_a, 2) - int(bin_b, 2)
        subt_binario = bin(subt_inteiro)
        c1 = complemento_a_1(bin_b)
        c2 = complemento_a_2(bin_b)
        print(print_zeros(bin_a), "->", a, " + ", print_zeros(bin_b), "->", b, "c1:", print_uns(c1), "c2:", c2,
              "=", print_zeros(subt_binario), "->", subt_inteiro)


soma(numeros)
subtracao(numeros)
