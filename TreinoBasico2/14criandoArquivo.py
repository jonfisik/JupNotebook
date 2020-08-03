# Escrevendo arquivos com funções python 03/08/2020 - jonatan paschoal

def EscreveArquivo():
    arquivo = open('NovoArquivo.txt', 'w+')
    arquivo.write('Linha gerada com função "EscreveArquivo" \r\n')
    arquivo.close

EscreveArquivo()

def AlteraArquivo():
    arquivo = open('NovoArquivo.txt', 'a+')
    arquivo.write('Linha gerada com função "ALteraArquivo" \r\n')
    arquivo.close

AlteraArquivo()