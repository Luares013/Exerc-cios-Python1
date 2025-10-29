#29 - Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as
#seguintes fórmulas:
#para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

#------------------------------------------------------------------

sexo=int(input("Digite seu sexo: 1 para masculino, 2 para feminino\n"))
altura=float(input("Digite sua altura (em Metros)\n"))

if sexo==1:
    pesoideal= (72.7*altura)-58

elif sexo==2:
    pesoideal= (62.1*altura)-44.7
   
print("Seu peso ideal é:\n", pesoideal)