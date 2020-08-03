# classe path 03/08/2020 - jonatan paschoal
#
from os import path
import time

def DadosArquivos():
    ArquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir("NovoArquivo.txt")
    pathArquivo = path.realpath("NovoArquivo.txt")
    pathRelativo = path.relpath("NovoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivos()