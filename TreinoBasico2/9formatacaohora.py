'''03/08/2020 - jonatan paschoal'''

from datetime import datetime
#
# formatado datas e horas
# Parâmetros: %y ou %Y - ano
# %a ou %A - dia da semana
# %b ou %B - Mês
# %d -  dia do mês
#
# %c - data e hora local
# %x - data local
# %X - hora da localidade
#
# %I ou %H - 12h ou 24h 
# %M - minuto
# %S - segundo
# %p - AM/PM
#
def FormataDataHora():
    hoje = datetime.now()
    
    print(hoje.strftime('O ano é: %y'))
    print(hoje.strftime('Data e hora local: %c'))
    print(hoje.strftime('A hora atual é: %I %M %S %p'))

FormataDataHora()

