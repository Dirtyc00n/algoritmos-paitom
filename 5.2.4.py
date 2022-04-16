#5.2.4. Crea un programa que pida su nombre
#al usuario y lo escriba centrado en pantalla
#(suponiendo que la pantalla tenga una anchura
#en mayúsculas y el resto en minúsculas
datos = [ [0 for columna in range(0,5)] for fila in range (0,4)]
datos[0][2] = 5
print(datos)
nombre = "espacio"
espacio = " "
apellido = "Juanez"
frase = nombre + espacio + apellido
nprint ( frase )
