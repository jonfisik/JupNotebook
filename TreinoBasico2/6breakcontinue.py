'''03/08/2020 - Jonatan Paschoal'''
# BREAK, CONTINUE

def loopBreak():
    for x in range(5,10):
        if x == 8:
            break
        print("O valor de x é: ", x)

loopBreak()

print('\n')

def loopContinue():
    for x in range(5,10):
        if x == 8:
            continue
        print('O valo de x é: ', x)

loopContinue()
