

def crearFuncion(n1,n2):
    
    def validacion():
        print('Genial')
        return n1 > 0 and n2 > 0

    return validacion

def aplicarFuncion(func):
    func

resultado = crearFuncion(111000,2)
aplicarFuncion(resultado)
print(resultado())