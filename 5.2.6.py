"""5.2.6. Crea un programa que pida al usuario
 10 palabras, las guarde en un array y luego le
  pregunte de forma repetitiva qué texto quiere
  buscar. Le responderá si dicho texto era alguno
  de lo que se habían introducido inicialmente.
  Dejará de repetirse cuando se introduzca "fin"."""
x=[]
for i in range (0,10):
    y=str(input("dime el dato palabra{}: ".format(i+1)))
    x.append(y)

z=int(input("ingresa el la palabra a consultar: "))

while z!=fin:
    if z in x:
        print("se encuentra en la lista")
    else:
        print("no se encuentra en la lista")
    z=int(input("ingresa el nombre a consultar: "))

