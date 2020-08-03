'''03/08/2020'''
# calendário
import calendar
# calendário tipo texto
def CalendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2020, 8)
    print(txtCalendario)

CalendarioTexto()

# calendário HTML
def CalendarioHTML():
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(2020, 8)
    print(htmlCalendario)

CalendarioHTML()