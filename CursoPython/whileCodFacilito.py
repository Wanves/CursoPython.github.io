contador = 0
bandera = True
while bandera:
    print(contador)
    contador += 1
    if contador == 10:
        print('Nivel 10 del contador')
        bandera = False
else:
    print('El ciclo a terminado')
