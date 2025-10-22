#2 - Faça um algoritmo que leia o nome e as notas
#dos 4 bimestres de um aluno.
#Posteriormente imprima o resultado de cada
#variável linha abaixo de linha.

#-------------------------------------------------

nome = input("Digite seu nome\n")
n1 = int (input("Digite a primeira nota:\n"))
n2 = int (input("Digite a segunda nota:\n"))
n3 = int (input("Digite a terceira nota:\n"))
n4 = int (input("Digite a quarta nota:\n"))

media = (n1+n2+n3+n4)/4

print("Seu nome é:\n", nome ,)
print("e sua média é:\n", media)
