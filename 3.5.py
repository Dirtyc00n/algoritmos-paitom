#3.5. Crea un programa que pida al usuario dos números reales y muestre el mayor de los dos (por ejemplo, si los números son -1.5 y 3.72, debería escribir en pantalla 3.72
num1=0
num2=0
print("Ingresa primer número")
num1 = float(input())
print("Ingresa segundo número")
num2 = float(input())
if num1>num2:
   print("el numero mayor es: ",num1)
else:
    if num2>num1:
     print("el numero mayor es: ",num2)
    else:
        print("los numeros son iguales", num1," = ", num2)
