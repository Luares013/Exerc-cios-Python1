#28 - Faça um Programa que peça 2 números inteiros e um número
#real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

#----------------------------------------


numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
numero3 = float(input('Digite um número real:'))

print(f'Resultado1: {(2*numero1)*(numero2/2)}')
print(f'Resultado2: {numero1 * 3 + numero3}')
print(f'Resultado3: {numero3*numero3*numero3}')
