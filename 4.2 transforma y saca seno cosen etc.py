"""4.2. Crea un programa que pida al usuario
 que introduzca un ángulo (en grados) y muestre
 su seno, su coseno y su tangente. Deberá repetirse
 hasta que el ángulo introducido sea de cero grados."""
import math
num = float(input("ingresa un angulo: "))
resultado = math.radians(num)
print ("El angulo es: ",resultado)
while num != 0:
    print ("su seno es: ",math.sin(resultado))
    print ("su coseno es: ",math.cos(resultado))
    print ("su tangente es: ",math.tan(resultado))
    num = float(input("ingresa un angulo"))
    resultado = math.radians(num)
