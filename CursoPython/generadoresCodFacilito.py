# def generador(*args):
#     for i in args:
#         yield i * 10
    
    
# for i in generador(55,25,63,6):
#     print(i, end='  ')
    
    
def multiplica(*args):
    for i in args:
        yield i*2
     
for i in multiplica(8,10,50,86):
    print(i)