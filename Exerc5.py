#5 - Faça um algoritmo que leia o nome do aluno,
#o nome da disciplina, notas de 3 provas e calcule
#a média desse aluno.
#Posteriormente imprima o resultado de cada
#variável linha abaixo de linha.

#---------------------------------------------------

nome = input("Digite seu nome:\n")
disciplina = input("Digite a disciplina:\n")
n1 = int (input("Digite a primeira nota:\n"))
n2 = int (input("Digite a segunda nota:\n"))
n3 = int (input("Digite a terceira nota:\n"))

media = (n1+n2+n3)/3

print("Seu nome é:\n",nome)
print("A materia avaliada é:\n",disciplina)
print("A media da disciplina", disciplina," é: ", media)
