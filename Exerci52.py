#52- Ler diversos números e exibir quantos foram digitados. O valor -1 é código de fim de entrada.

quantidade = 0

numero=int(input("Digite um numero:(digite -1 para encerrar)\n"))
quantidade= quantidade+1

while quantidade!=-1:
    numero=int(input("Digite um numero:(digite -1 para encerrar)\n"))
    
    if numero!=-1:
       quantidade=quantidade+1
       
    print("A quantidade de numeros digitados foram \n", quantidade) 