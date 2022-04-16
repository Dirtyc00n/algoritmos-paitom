#5.2.3. Crea un programa que pida su nombre
# al usuario y diga cuántas vocales contiene
nombre = input( "Dime tu nombre: " )
print ( "Con espacios sería" )
for i in range(0, len(nombre)):
    print ( nombre[i], end="" )
    print ( " ", end="" )
print()
print("Y las letras 2ª a 4ª son:")
print(nombre[1:5])
