def leerARchivos():
    file = open('data1.txt', 'r')
    lineas = file.readlines()
    print(lineas)
    #print(file)
    file.close()
#leerARchivos()

def withOpen():
    with open('data2.txt','r')as archivo:
        lineas = archivo.readlines()
        print(lineas)
    for i in lineas:
        print(i.replace('\n', ''))

withOpen()

def withOpen():
    with open('data2.txt','r')as archivo:
        contenido = archivo.read()
        lineas = contenido.split('\n')
        print(lineas)
withOpen()

def withOpen():
    with open('data2.txt','r')as archivo:
        contenido = archivo.read()
        lineas = contenido.split('\n')
        pos = archivo.tell()
        print(pos)
        print(f'El archivo tiene {pos} caracteres de longitud')
withOpen()

def seek():
    with open('data2.txt','r')as archivo:
        archivo.seek(7)
        pos = archivo.tell()
        print(pos)
        contenido = archivo.read()
        lineas = contenido.split('\n')
        print(lineas)
seek()

def siguientesAleer():
    with open('data2.txt','r')as archivo:
        siguientes15 = archivo.read(15)
        print(siguientes15)
        print(type(archivo.read()))
siguientesAleer()

def siguientesAleer2():
    with open('data2.txt','rb')as archivo:
        siguientes15 = archivo.read(15)
        print(siguientes15)
        print(type(archivo.read()))
siguientesAleer2()

def write():
    with open('data2.txt','w')as archivo:
        archivo.write('Hacemos de algo simple algo extraordinario\n')
        archivo.write('Nunca pares de aprender\n')
        archivo.write('Genial!!!')
        print('Escritura exitosa')
write()