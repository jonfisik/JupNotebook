'''03/08/2020'''
#definindo o LOOPR FOR
def loopfor():
    for x in range(5,11):
        print(x, end = ' ')

loopfor()
print('\n')

#LOOP FOR com coleção
def loopArray():
    dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    for d in dias:
        print(d, end = ' ')

loopArray()
print('\n')

# função enumerate
def loopEnum():
    dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    for i, d in enumerate(dias):
        print(i, d, end = ' ')

loopEnum()

