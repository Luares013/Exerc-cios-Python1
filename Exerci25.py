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


