

# def palindromo():
#     nuevoValor = frase.replace(' ','')
#     return nuevoValor == nuevoValor[::-1]


# frase = 'somos o no somos'
# print(frase)
# resultado = palindromo()
# print(frase)
# print(resultado)


# def valorGlobal():
#     global variableGlobal
#     variableGlobal = 'Cambiar Valor, Genial'
    
    
# def mostrarGlobal():
#     print(variableGlobal)

# variableGlobal = 'Esto es una variable global'
# print(variableGlobal)
# mostrarGlobal()
# valorGlobal()
# print(variableGlobal)


# saludo = 'Genial'

# def saludar():
#     global saludo
#     saludo = 'Esto es Genial!'
#     # saludo


# saludar()
# print(saludo)

# def suma(*args):
#     resultado = 0
#     for i in args:
#         resultado = resultado + i
#     return resultado
        

# resultado = suma(10,5,30,20,50)
# print(resultado)


# def suma(*args):
#     resultado = 0
#     for i in args:
#         resultado +=i
#     return resultado




# resultado = suma(1000,2000,3000,5000)
# print(resultado)

# def concatena(*args):
#     resultado = [' ','*']
#     for i in args:
#         resultado +=i
#     return resultado

# resultado = concatena(' Genial ',' lo ',' haces ',' muy bien! ')
# print(resultado)
    
def suma(**kwargs):
    # dato = kwargs.get('c','No contiene el dato')
    # print(dato)
    print(kwargs)
    print(list(kwargs))
    
resultado = suma(a= ' Genial ',b= ' lo',c=' haces',d=' muy bien')
print(resultado)









