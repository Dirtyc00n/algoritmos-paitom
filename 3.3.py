#3.3. Crea un programa que pida al usuario un número entero y le responda si es positivo, negativo o cero
num1=0
print("ingresa un numero")
num1=int(input())
if num1>0:
    print("El número es positivo")
else:
    if num1<0:
        print("el número es negativo")
    else:
        print("el número es 0")

