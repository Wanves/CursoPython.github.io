import random
from werkzeug.security import generate_password_hash
minusculas = 'abcdefghijklmnñopqrstuvwxyz'
mayusculas = minusculas.upper()
numeros = '0123456789'
simbolos = '!"#$%&/()=?¡/*-+'
longitud = 12

base = minusculas + mayusculas + numeros + simbolos


for _ in range(5):
    muestra = random.sample(base, longitud)
    password = ''.join(muestra)
    password_encriptado = generate_password_hash(password)
    print(f'{password} -> {password_encriptado}')
