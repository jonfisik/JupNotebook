# manipulando arquivos - criando arquivos compactados
# 03/08/2020 - jonatan paschoal
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

# compactar arquivo
def CriaZipModo1(): 
    shutil.make_archive('ArquivoCompactado', 'zip', 'E:\\CURSOS\\REPOSITORIOS\\REP_GIT_PY\\JupNotebook\\TreinoBasico2\\teste')

### CriaZipModo1()

# compactar arquivo modo 2
def CriaZipModo2():
    with ZipFile('ArquivoZipModo2.zip', 'w') as novoZip:
        novoZip.write('ArquivoAlterado.txt')
        novoZip.write('NovoArquivo.txt')
        novoZip.write('ArquivoCompactado.zip')

###CriaZipModo2()

# deletando arquivo
def DeletaArquivo():
    os.remove('ArquivoZipModo2.zip')

DeletaArquivo()


