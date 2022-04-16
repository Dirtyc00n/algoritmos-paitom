"""4.3. Crea un programa que pida un código de usuario
 y una contraseña. No se le dejará proseguir hasta que
  el código sea 1234 y la clave sera 5000."""
codigo = int(input("ingresa un codigo de usuario: "))
while codigo !=1234:
    codigo = int(input("ingresa un codigo de usuario: "))
print("el codigo de usuario es correcto")
clave = int(input("ingresa una clave de usuario: "))
while codigo !=5000:
    codigo = int(input("ingresa una clave de usuario: "))
print("la clave de usuario es correcto")
