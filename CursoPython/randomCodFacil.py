# import random

# # num = random.randint(0,11)
# # print(num)

# list = [True,'String',23, False]
# # dato = random.choice(list)

# print(list)
# random.shuffle(list)
# print(list)

# import datetime

# print(datetime.datetime.now())


# import sys
# import time
# for i in range(100):
#     time.sleep(.5)
#     sys.stdout.write('\r%d %%' % i)
#     sys.stdout.flush()

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Necesario colocar mínimo un argumento')
    else:
        print(sys.argv[1]=='help')