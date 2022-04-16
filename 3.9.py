#3.9. Crea un programa que pida al usuario un número real y muestre su raíz cuadrada (si es positivo) o un aviso de que no se puede calcular la raíz cuadrada (si es negativo)
import math
num1=0
print("Ingresa un numero :")
num1=float(input())
if num1>=0:
  print("Raíz de ",num1," es: ",math.sqrt(num1))
else:
	print("No se puede calcular la raiz cuadrada de un número negativo")
	
