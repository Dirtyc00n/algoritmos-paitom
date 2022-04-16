"""5.2.5. Crea un programa que pida al usuario
10 palabras y luego las muestre de la última a la primera"""

datos = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    datos[i-1] = str(input( "Dime el dato numero {}: ".format(i) ))
print ("Los datos al reves son: ")
for i in range(9,0,-1):
    print ( datos[i-1] )
