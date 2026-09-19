notas = [16, 18, 12, 15, 19]
suma =0
for nota in notas:
    suma = nota + suma
    promedio = suma / len(notas)
    print("nota: ", nota)
print("promedio: ", promedio)