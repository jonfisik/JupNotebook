# leitura de arquivos com python 03/08/2020 - jonatan paschoal

def leituraArquivo():
    arquivo = open('NovoArquivo.txt', 'r')
    if(arquivo.mode == 'r'):
        conteudo = arquivo.read()
        print(conteudo)
    
    arquivo.close()

#leituraArquivo()
# leitura linha a linha de conteudo extenso
def leituraArquivoExtenso():
    arquivo = open('NovoArquivo.txt', 'r')
    if(arquivo.mode == 'r'):
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal: 
            print(conteudo)
    
    arquivo.close()

leituraArquivoExtenso()