def operaciones():
    num1 = float(input('Ingresa el primer número seleccionado-> '))
    num2 = float(input('Ingresa el segundo número seleccionado-> '))
    operacion = input(f'''
                      Ingresa la operación seleccionada:
                      a. suma
                      b. resta
                      c. multiplica
                      d. divide
                      e. potencia
                      f. modulo
                      ''')
    if operacion == 'a':
        print(num1 + num2)
    elif operacion == 'b':
        print(num1 - num2)
    elif operacion == 'c':
        print(num1 * num2)
    elif operacion == 'd':
        print(num1 / num2)
    elif operacion == 'e':
        print(num1 ** num2)
    else:
        print(num1 % num2)

operaciones()