lista = ['auto', 'moto', 'avión', 'tren']
lista2 = [1,2,3,4,5,6,7,8,9,10]

print(lista)

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[0:2])
print(lista[:2])
print(lista[2:])
print(lista + lista2)
print(tuple(lista))
print(set(lista))
del lista2[5]
del lista[-1]
print(lista2)
print(lista)

print(4%2)
print(3%2)

a = int(input('Ingresa el primer número-> '))
b = int(input('Ingresa el segundo número-> '))
if a == b:
  print('Ingresa dos números diferentes-> ')
else:
  if a > b:
    c = a
    a = b
    b = c

  i = 1
  for i in range(a+i,b):
    
    print(i)


