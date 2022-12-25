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


def opMultiplica():
    n1 = int(input('ingresa el primer número-> '))
    n2 = int(input('ingresa el segundo número-> '))
    multiplica = n1 * n2
    print(multiplica)


def opDivide():
    n1 = int(input('ingresa el primer número-> '))
    n2 = int(input('ingresa el segundo número-> '))
    divide = n1 / n2
    print(divide)


def elegirOperacion():
    operacion = input(f'''
   Ingresa operación->
    1. suma,
    2. resta,
    3. multiplica
    4. divide
    ''')
    if operacion == '1':
        return opSuma()
    elif operacion == '2':
        return opResta()
    elif operacion == '3':
        return opMultiplica()
    elif operacion == '4':
        return opDivide()
    else:

        while operacion != '1' or operacion != '2' or operacion != '3' or operacion != '4':
            print('Elige una opción')
            operacion = input(f'''
                   Ingresa operación->
                   1. suma,
                   2. resta,
                   3. multiplica
                   4. divide
                   ''')
            if operacion == '1':
                return opSuma()
            elif operacion == '2':
                return opResta()
            elif operacion == '3':
                return opMultiplica()
            elif operacion == '4':
                return opDivide()


elegirOperacion()
