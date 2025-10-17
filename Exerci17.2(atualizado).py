17 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e reajuste-o seguindo o
seguinte critério baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe
na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

-----------------------------------------------------

salario = float(input("Digite seu salario\n"))

if salario<=280:
    percentual="20%"
    aumento= salario*20/100
    
elif salario>280 and salario<=700:
    percentual="15%"
    aumento= salario*15/100
    
elif salario>700 and salario<+1500:
    percentual="10%"
    aumento= salario*10/100
    
else:
    percentual="5%"
    aumento= salario*5/100
    
 
print("seu salario anterior era:",salario)
print("Percentual de aumento foi:", percentual)
print("O valor do aumento foi:", aumento)
print("O novo salario apos aumento e:", (salario+aumento))
