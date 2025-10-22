#IDADE TIPO
#0-2 anos bebê
#3-11 anos Criança
#12-21 anos Jovem
#22-64 anos Adulto
#65-100 anos Idoso
#Acima de 101 anos Muito velhinho

#------------------------------------------------------

nome = input("Digite o nome da pessoa:\n")
idade = int(input("Digite sua idade:\n"))

if (idade<=2): print(nome,"é um bebe")
elif(idade>=3 and idade<=11): print(nome,"é uma criança")
elif(idade>=12 and idade<=21): print(nome,"é um jovem")
elif(idade>=22 and idade<=64): print(nome,"é um adulto")
elif(idade>=65 and idade<=100): print(nome, "é um idoso")
elif(idade>101): print(nome, "é um muito velhinho")
else: print("Erro")
