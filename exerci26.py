#26 - Um brechó revende produtos usados, e fixa o preço de
#venda de cada produto conforme o valor de sua aquisição: Se o
#preço de aquisição de um produto é menor que R$ 50,00, ele
#deve ser vendido por um preço 45% maior, caso contrário o lucro
#será de 30%. Sabendo disso, faça um algoritmo que leia o valor
#de aquisição de um produto e mostre o seu valor de venda.

#---------------------------------------------------------

aquisição= float(input("Digite o preço que foi pago pela peça:\n"))

if aquisição <50:
    lucro= aquisição*45/100
    
elif aquisição >= 50:
    lucro=aquisição*30/100
    
venda= aquisição+lucro

print("O valor que a peça deve ser vendida é:  ", venda)