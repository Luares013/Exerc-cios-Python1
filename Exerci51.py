#51- Ler diversos números e exibir qual foi a soma.
#O valor -999 é o código de fim da entrada.

#------------------------------------------------------------------------

soma=0
numero =int(input("Digite um numero:(digite -999 para encerrar a soma)\n"))

while numero!= -999:
    numero =int(input("Digite um numero: (digite -999 para encerrar a soma)\n"))

    if  numero!= -999:  
        soma= soma+numero 

print("A soma dos numeros digitados foram:\n", soma)   


