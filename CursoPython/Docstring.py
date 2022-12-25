


def generador(*args):
    '''
    Se trata de comentar los proyectos es una buena práctica
    Se trata de comentar los proyectos es una buena práctica
    Se trata de comentar los proyectos es una buena práctica
    '''
    for valor in args:
        yield valor, True if valor > 5 else False


nombre = generador.__name__
comentado = generador.__doc__

print(f'{nombre} contiene la siguiente documentación:')
print(comentado)