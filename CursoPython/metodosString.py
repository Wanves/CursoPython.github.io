curso = 'Genial'
myString = 'Lo haces muy bien'

def formato():
    print(f'{curso} {myString}')
    print(myString[0:3])
    print(myString[6])
    print(f'{curso} {myString}'.lower())
    print(f'{curso} {myString}'.upper())
    print(f'{curso} {myString}'.capitalize())
    print(f'{curso} {myString}'.split())
    print(f'{curso} {myString}'.title())
    print(f'{curso} {myString}'.casefold())
    print(myString[::-1])
    print(len(myString))
    print(myString.replace('','*'))
    print(myString.split())
    
# def __str__():
#     print(f'{curso}  {myString}'.lower())
#     print(f'{curso}  {myString}'.upper())
#     print(f'{curso}  {myString}'.capitalize())
#     print(f'{curso}  {myString}'.split())
#     print(f'{curso}  {myString}'.title())
#     print(f'{curso}  {myString}'.casefold())

a = myString.find('e')
count = myString.count('bien')
print(a)
print(count)
#__str__()
formato()
