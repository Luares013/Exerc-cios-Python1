#10 - Faça um algoritmo que verifique se o número
#digitado é menor, maior ou igual a 10 e apresente
#a mensagem referente ao número.

#----------------------------------------------------

numero = int(input("Digite um numero :\n"))

if(numero>10): print("Esse numero",numero, "é maior que 10")
elif (numero<10): print("Esse numero",numero,"é menor que 10")
else: print("O numero digitado é 10")
