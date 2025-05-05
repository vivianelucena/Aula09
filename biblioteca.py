def imprime_nome(nome):
    print(f'Nome: {nome}.')

#exercicio01
def piramide(x):
    for a in range(1, x+1, 1):
        for b in range(0, a):
            print(a, end=' ')
        print()

#exercicio02
def piramide2(x):
    for a in range(1, x+1, 1):
        for b in range(0, a):
            print(b, end=' ')
        print()

#exercicio03
def vogais(texto):
    cont = 0
    novoTexto = texto.lower
    for a in texto:
        if a in 'aeiou': #if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
            cont = cont + 1
    print(f'Tem {cont} vogais!')

#exercicio04
def produtos(nome, quantidade, valor):
    estoque = quantidade*valor
    print(f'O valor total do estoque é: R${estoque:.2f}')

#exercicio05
def produto(nome, quantidade, valor):
    estoque = quantidade*valor
    return nome, quantidade, valor, estoque

def argumento(arg):
    if arg < 0:
        return 'N'
    elif arg > 0:
        return 'P'
    else:
        return 'Z'

def soma(a, b):
    resposta = a + b
    return resposta

def somarItens(*itens):
    for a in itens:
        soma = sum(itens)
    print(soma)

def texto_reverso(letras):
    cont=0
    for a in range(len(letras) -1, -1, -1):
        if letras[a] != ' ':
            cont = cont + 1
        print(letras[a], end =' ')
    print(cont)

def lista(parametro):
    novaLista = []
    for a in parametro:
        if a not in novaLista:
            novaLista.append(a)
    print(novaLista)

def lista2(parametro):
    novaLista= []
    novaLista = set(parametro)
    print(novaLista)