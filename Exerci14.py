#14 - Faça um algoritmo para ler: número da conta
#do cliente, saldo, débito e crédito. Após, calcule e
#escreva o saldo atual (saldo atual = saldo - débito
# crédito). Também teste se saldo atual for maior
#ou igual a zero. Em seguida escreva a mensagem
#'Saldo Positivo', senão, escrever a mensagem
#'Saldo Negativo' .

#---------------------------------------

nconta = int(input("Digite o numero da conta:\n"))
saldo = int(input("Digite o saldo da conta:\n"))
debito = int(input("Digite quanto foi debitado da conta:\n"))
credito = int(input("Digite quanto foi creditado na conta:\n"))

saldoatual = (saldo-debito+credito)
if(saldoatual>0): print("Seu saldo atual é positivo")
elif(saldoatual <0): print("Seu saldo atual é negativo")
else: print("Seu saldo é nulo")
