x=[]
for i in range (0,10):
    y=int(input("dime el dato numero{}: ".format(i+1)))
    x.append(y)

z=int(input("ingresa el numero a consultar: "))
count=0
while z!=0:
    if z in x :
        for a in range (0,10):
            if z==x[a]:
                count+=1

        print("se encuentra en la lista")
        print("se encontro",count,"veces")

    else:
        print("no se encuentra en la lista")
    count=0
    z=int(input("ingresa el numero a consultar: "))



