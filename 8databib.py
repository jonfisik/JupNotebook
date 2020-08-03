'''03/08/2020 - jonatan paschoal'''
from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
    hoje = date.today()
    print(f'Hoje é {hoje}.')
    print(f'Partes da data -> dia {hoje.day} - mês {hoje.month} - ano {hoje.year}.')
    print(f'Número do dia da semana: {hoje.weekday()+2}')
    dias = ['dom','seg','ter','qua','qui','sex','sab']
    print('Nome abreviado do dia da semana: ', dias[hoje.weekday()+1])
    
    data = datetime.now()
    print('Data e hora: ', data)

    tempo = datetime.time(data)
    print('Hora atual: ', tempo)

ManipulaDataHora()