#15 - Faça um Programa que verifique se uma
#letra digitada é "F" ou "M". Conforme a letra
#escreva: F - Feminino, M – Masculino ou Sexo
#Inválido.

#--------------------------------------------------------

letra = input("Digite seu genero (F ou M):\n")

if (letra =="F" or letra=="f"):print("Seu genero é feminino")
elif (letra =="M" or letra=="m"): print("Seu genero é masculino")
else: print("Sexo invalido")
