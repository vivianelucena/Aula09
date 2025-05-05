from biblioteca import *      # piramide, piramide2, vogais, produtos, produto, argumento, soma

print('Exercicio 01')
piramide(4)

print()

print('Exercicio 02')
piramide2(4)

print()

print('Exercicio 03')
vogais('o rato roeu a roupa do rei de roma')

print()

print('Exercicio 04')
produtos('caneta', 10, 3.5)

print()

print('Exercicio 05')
arroz = produto("arroz", 5, 10)
print(f'O valor do estoque de arroz é: {arroz[3]}')
print(arroz)

print()

print('Exercicio 06')
valor = int(input('Digite um número: '))
print(argumento(valor))

print()

print('Exercicio 07')

numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número:'))
print(soma(numero1,numero2))

print()

print('Exercicio 08')
print(somarItens(20, 20, 5, 5))

print()

print('Exercicio 09')
texto_reverso('o rato roeu a roupa do rei de roma')

print()

print('Exercicio 10')
lista([10, 12, 12, 31, 4, 4, 5, 31, 6, 7, 6, 8])

print()

print('Exercicio 11')
lista2([10, 12, 12, 31, 4, 4, 5, 31, 6, 7, 6, 8])