22 -Faça um algoritmo que receba o preço de um
produto, calcule e mostre o novo preço, sabendose que este sofreu um desconto de 10%.


-------------------------------------------------------------------------------------------------------------


valorproduto= float(input("Digite o valor do produto que deseja compra(sabendo que esta na mega oferta 10%)\n"))

desconto= valorproduto*10/100

valortotal=valorproduto-desconto

print("O valor do desconto foi:\n", desconto)
print("O valor total com o desconto de 10% é:\n", valortotal)
