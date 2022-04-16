#3.8. Crea un programa que pida al usuario dos números enteros y los muestre ordenados (primero el menor de ellos y luego el mayor de ellos)
num1=0
num2=0
print("Ingresa primer número")
num1 = int(input())
print("Ingresa segundo número")
num2 = int(input())
if num1>num2:
   print(num2," - ", num1)
else:
    print(num1," - ", num2)
