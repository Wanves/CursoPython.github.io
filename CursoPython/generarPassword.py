import random
from werkzeug.security import generate_password_hash
minus = 'abcdefghijklmnñopqrstuvwxyz'
mayus = minus.upper()
numeros = '0123456789'
simbolos = '@/[]{}()*-+?¡¿!<>_-:.;,='
base = minus+mayus+numeros+simbolos
longitud = 12


for _ in range(6):
    muetra = random.sample(base,longitud)
    password = ''.join(muetra)
    passwordEncriptado = generate_password_hash(password)
    print(f'{password} => {passwordEncriptado}')