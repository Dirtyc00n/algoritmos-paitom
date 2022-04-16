x=[]
for i in range (0,10):
    y=int(input("dime el dato numero{}: ".format(i+1)))
    x.append(y)

z=int(input("ingresa el numero a consultar: "))

while z!=0:
    if z in x:
        print("se encuentra en la lista")
    else:
        print("no se encuentra en la lista")
    z=int(input("ingresa el numero a consultar: "))
