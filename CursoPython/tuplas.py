



# l2 = [1,'Juan',56.5,.3,True,False,5j]
# l2.insert(4,'Lio')
# print(l2)

# nombre = input('Ingresa el nombre ')
# edad = int(input('Ingresa tu edad '))
# resultado = edad + 20
# print(f'Tu edad futura es: {resultado}')
# print(f'Tu nombre es: {nombre} y tu edad es {edad}')

from argon2 import DEFAULT_TIME_COST


print('Operaciones')
a = int(input('Ingresa el primer número-> '))
b = int(input('Ingresa el segundo número-> '))
Menu = input(f'''Ingresa la operación seleccionada-> 
             1. suma
             2. resta
             3. multiplica
             4. divide
        ''') 
if Menu == '1':
    print(f'El resultado de la suma es: {a + b}')
elif Menu == '2':
    print(f'El resultado de la resta es: {a - b}')
elif Menu == '3':
    print(f'El resultado de la multiplicación es: {a * b}')
else:
    print(f'El resultado de la división es: {a / b}')



