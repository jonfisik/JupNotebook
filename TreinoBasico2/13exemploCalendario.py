'''03/08/2020 - jonatan paschoal'''
import calendar

def ImprimeMes():
    print('-'*8)
    for mes in calendar.month_name:
        print(mes)
    print('-'*8)
    for dia in calendar.day_name:
        print(dia)
    print('-'*8)

ImprimeMes()