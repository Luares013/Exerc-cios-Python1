#19 -Faça um Programa que peça os 3 lados de
#um triângulo. Indique, caso os lados formem um
#triângulo, se o mesmo é: equilátero, isósceles ou
#escaleno.

#------------------------------------------------

print("VAMOS FORMAR UM TRIANGULO E VER QUAL TIPO DE TRIANGULO ELE SERA")

lado1=int(input("Digite o lado 1 do triangulo:\n"))
lado2=int(input("Digite o lado 2 do triangulo:\n"))
lado3=int(input("Digite o lado 3 do triangulo:\n"))

if lado1==lado2==lado3:
    Triangulo="Equilátero"
    
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    Triangulo="Isósceles"
    
elif lado1!=lado2!=lado3:
    Triangulo="Escaleno"
    

print("O triangulo tem os lados:\n", lado1, lado2,lado3, "\n e o triangulo formado é:\n", Triangulo)

