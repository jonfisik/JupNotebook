# 03/08/2020 - JonatanPaschoal

#declarando funções
def func1():
    print('-'*18)
    print('Eu sou uma função.')
    print('-'*18)

func1() #chamando as função e seus argumentos entre parênteses

# função e recebe argumentos
def func2(arg1,arg2):
    print(arg1 + " " + arg2)
    print('-'*18)

func2('Jonatan', 'Paschoal')

# função retorna valor
def cubo(x):
    return x * x * x
    
cubo(3) # apenas excuta a função

f = cubo(3) # atribui-se o valor da função a uma variável
print(f)
print('-'*18)# ou
print(f'Volume = {cubo(2)}')
print('-'*18)