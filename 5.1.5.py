#5.1.5
b=[]
for f in range (0,5):
    a=int(input("ingresa numeros {}:".format(f+1)))
    b.append(a)
menor=1000000
for i in range (0,5):
    if menor > b[i]:
        menor=b[i]
print("el menor es ",menor)
