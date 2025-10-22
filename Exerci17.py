#17 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
#colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e reajuste-o seguindo o
#seguinte critério baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
# valor do aumento;
#o novo salário, após o aumento.

#-------------------------------------------------------

salario = float(input("Digite seu salario\n"))

if(salario<=280): 
    print("Seu salario antes do reajuste e\n", salario,
"\nO percentual de aumento foi 20%", "\nO valor do aumento foi\n", salario*20/100, 
"\no novo salario, apos o aumento é\n", salario+(salario*20/100))

elif(salario >280) and (salario<=700):
    print("Seu salario antes do reajuste e\n", salario,
"\nO percentual de aumento foi 15%", "\nO valor do aumento foi\n", salario*15/100, 
"\no novo salario, apos o aumento é\n", salario+(salario*15/100))
    
elif(salario >700) and (salario<=1500):
    print("Seu salario antes do reajuste e\n", salario,
"\nO percentual de aumento foi 10%", "\nO valor do aumento foi\n", salario*10/100, 
"\no novo salario, apos o aumento é\n", salario+(salario*10/100))
    
else:
    print("Seu salario antes do reajuste e\n", salario,
"\nO percentual de aumento foi 5%", "\nO valor do aumento foi\n", salario*5/100, 
"\no novo salario, apos o aumento é\n", salario+(salario*5/100))
