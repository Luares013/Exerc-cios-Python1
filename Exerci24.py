#24- A lanchonete GostoSoft vende apenas um tipo de sanduíche,
#cujo recheio inclui duas fatias de queijo, uma fatia de presunto e
#uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou
#presunto pesa 50 gramas, e que a rodela de hambúrguer pesa
#100 gramas, faça um algoritmo em que o dono forneça a
#quantidade de sanduíches a fazer, e a máquina informe as
#quantidades (em quilos) de queijo, presunto e carne necessários
#para compra.

#----------------------------------------------------

#lanche : 2 QJ, 1 Presunto, 1 Hamb 
#Qj ou Presunto: 50g
#hamb: 100g

queijo=50*2
presunto=50
hamburguer=100
queijo_KG= queijo/1000
presunto_KG= presunto/1000
hamburguer_KG= hamburguer/1000

sanduiche= int(input("digite a quantidade de sanduiche:\n"))

Total_queijo= sanduiche*queijo_KG
total_presunto= sanduiche*presunto_KG
total_hamburguer= sanduiche*hamburguer_KG

print("==============================================================")

print("A quantidade de queijo em KG nescessarios é:       ", Total_queijo)
print("A quantidade de presunto em KG nescessario é :      ", total_presunto)
print("A quantidade de carne para o hamburguer em KG é :   ", total_hamburguer)

print("==============================================================")
