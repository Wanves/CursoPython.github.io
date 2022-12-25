
"""
lista = []
for valor in range(0,21):
    lista.append(valor)
"""

lista = [ i for i in range(0,21) if i % 2 == 0]
tuple = tuple(i for i in range(0,21) if i % 2 == 0)
dic = {indice:i for indice, i in enumerate(lista) if indice < 5}
print(lista)
print(tuple)
print(dic)