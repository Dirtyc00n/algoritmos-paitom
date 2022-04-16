
"""4.5. Crea un programa que pida al usuario un número entero
(por ejemplo, 5) y muestra la tabla de multiplicar de ese número
(desde "5x1=5" hasta "5x10=50")."""

x=int(input("Ingrese un numero intero: "))
i=1
for i in range (1, 11,1):
    print("", x,"*",i,"=",x*i)
