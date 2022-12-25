# def potencia(n):
#     return pow(n, 3)

# numeros = list(range(1,11))
# print(numeros)
# elevarLista = list(map(potencia, numeros))
# print(elevarLista)
# for numeros in elevarLista:
#     print(numeros,end=' ')


# def potencia(n):
#     return pow(n, 3)
# potencia = lambda n: pow(n, 2)


# numeros = list(range(1,11))
# print(numeros, 'Lista')
# print('==============')
# elevarLista = list(map(potencia,numeros))
# print(elevarLista, 'Lista elevada')


potencia = lambda n: pow(n,2)

numeros = list(range(1,11))
print(numeros)
# elevarNumeros = list(map(potencia,numeros))
# print(elevarNumeros)
elevarNumeros = map(potencia,numeros)
for numeros in elevarNumeros:
    print(numeros,end=' ')