#3.7. Crea un programa que pida al usuario tres números reales y muestre el mayor de los tres
num1=0
num2=0
num3=0
print("Ingresa primer número")
num1 = float(input())
print("Ingresa segundo número")
num2 = float(input())
print("Ingresa tercer número")
num3 = float(input())
if num1>num2 and num1>num3:
   print("El numero mayor es: ",num1)
else:
    if num2>num1 and num2>num3:
        print("El numero mayor es: ",num2)
    else:
     print("El numero mayor es: ",num3)


