20 -Faça um Programa que peça um número
correspondente a um determinado ano e em
seguida informe se este é bissexto. 

---------------------------------------------------

ano=int(input("Digite o ano que quer analisar:\n"))

if (ano %4 ==0 and ano %100 !=0) or ano %400 == 0:
    ano=" É Bissexto"
else:
    ano= "Não é bissexto"


print("o ano",ano)
