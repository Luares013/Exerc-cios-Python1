#21 -Um funcionário recebe um salário fixo mais
#4% de comissão sobre vendas. Faça um
#algoritmo que receba o salário fixo de um
#funcionário e o valor de suas vendas, calcule e
#mostre o valor da comissão e o salário final do
#funcionário.


#-----------------------------------------------------------------------


salariobase= float(input("Digite seu salario base:\n"))
vendas= float(input("Digite o total em vendas que voce fez no mes:\n"))
              
comissao= (vendas *4/100)
salariototal= salariobase+comissao


print("Total em comissao foi:\n", comissao )
print("O total com comissao é:\n", salariototal)
