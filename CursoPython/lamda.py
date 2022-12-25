
# sumar = lambda n1, n2: n1 + n2

# print(sumar(5,60))



def opSuma():
    n1 = int(input('ingresa el primer número-> '))
    n2 = int(input('ingresa el segundo número-> '))
    suma = n1 + n2
    print(suma)


def opResta():
    n1 = int(input('ingresa el primer número-> '))
    n2 = int(input('ingresa el segundo número-> '))
    resta = n1 - n2
    print(resta)


def elegirOperacion():

   operacion = input('Ingresa operación-> 1. suma, 2. resta')
   if operacion =='1':
       return opSuma()
   elif operacion =='2':
       return opResta()
   else:
       print('Elige operacion')
    
    
elegirOperacion()

