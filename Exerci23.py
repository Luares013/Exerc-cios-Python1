
#23 - A granja TecFrango possui um controle automatizado de
#cada frango da sua produção. No pé direito do frango há um anel
#com um chip de identificação, no pé esquerdo são dois anéis para
#indicar o tipo de alimento que ele deve consumir. Sabendo que o
#anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50,
#faça um algoritmo para calcular o gasto total da granja (com base
#na quantidade de frangos digitada pelo usuário) para marcar todos
#os seus frangos.

#-----------------------------------------------------------------------------

anel_chip=4
anel_normal= 3.5*2

frangos= int(input("Digite a quantidade de frangos que tem na granja:\n"))
valor_por_frango = (anel_chip+anel_normal)*frangos

print("================================================================")

print("O valor gasto para indentificação geral da granja é:", valor_por_frango)

print("================================================================")
