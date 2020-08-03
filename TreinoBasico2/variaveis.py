# 03/08/2020 - JonatanPaschoal

# declarando e inicializando variáveis;
print('-'*5)
f = 0
print(f'{f:^5}')

# declarando a mesma vaariável mais de uma vez;
print('-'*5)
f = 'abc'
print(f'{f:^5}')
print('-'*33)

# fazendo concatenação
print('String ligada a string ' + str('0123456789'))
print('-'*33)

# variável global x variável local
def NomeFuncao(): #definição de função
    f = 'ABC' # 'f' está declarada como variável local
    print(f'{f:^5}')
NomeFuncao()

print(f'{f:^5}')
print('-'*5)

'''def NomeFuncao():
    global f
    f = 'ABCD'
    print(f'{f:^5}')
NomeFuncao()'''
print('-'*5)