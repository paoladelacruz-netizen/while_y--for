venta = 0
cantidad = 0
total = 0
venta =float(input("Ingrese el valor de ventas: "))
while venta != 0:
    cantidad = cantidad + 1
    total =venta + total 
    venta =float(input("Ingrese el valor de ventas: "))
print ("cantidad de ventas: ", cantidad)
print("total de ventas: ", total)