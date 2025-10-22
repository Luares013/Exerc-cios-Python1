#25 - Uma fábrica de camisetas produz os tamanhos pequeno,
#médio e grande, cada uma sendo vendida respectivamente por
#R$10,00, R$12,00 e R$15,00. Faça um algoritmo em que o
#usuário forneça a quantidade de camisetas pequenas, médias e
#grandes referentes a uma venda, o algoritmo informe qual o valor
#total da compra.

#---------------------------------------------------------------------------------------

preço_pequena = 10
preço_media= 12
preço_grande= 15

camiseta_P= int(input("Digite a quandidade de camisetas pequenas voce deseja:\n"))
camiseta_M= int(input("Digite a quandidade de camisetas medias voce deseja:\n"))
camiseta_G= int(input("Digite a quandidade de camisetas grandes voce deseja:\n"))

total_P= preço_pequena*camiseta_P
total_M= preço_media*camiseta_M
total_G= preço_grande*camiseta_G

valor_total= total_G+total_M+total_P

print("valor total da compra é:\n", valor_total)


