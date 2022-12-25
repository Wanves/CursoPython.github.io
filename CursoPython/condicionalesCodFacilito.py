

valor = int(input('Ingresa un valor: '))
valor2 = int(input('Ingresa un valor: '))
valor3 = valor + valor2

if valor3 < 50:
    print(f'Es un valor monor a 50 y es: {valor3}')
elif valor3 < 100:
    print(f'Es un valor menor a 100 y es: {valor3}')
else:
    print(f'Es un valor mayor a 100 y es: {valor3}')