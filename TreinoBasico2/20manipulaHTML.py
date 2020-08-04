# processamento e parse de HTML - 04/08/2020 - jonatan paschoal

from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Tag de abertura encontrada!')
        if attrs.__len__() > 0:
            for a in attrs:
                print('  VAlores encontrados: ', a[0], " = ", a[1])
    
    def handle_endtag(self, tag):
        print('Tag de fechamento encontrada.')
    
    def handle_comment(self, data):
        print('Comentário encontrado.')
    
    def handle_data(self, data):
        print('Valores encontrados.')
        if data.isspace():
            print('O valor encontrado é um espaço.')
        else:
            print('O valor encontrado é: ', data)

def meuObjeto():
    meuparser1 = meuParser()
    arquivo = open('E:\\CURSOS\\REPOSITORIOS\\REP_GIT_HTML\\ProjetosWeb_2020\\ProjetoWeb3_2020\\ModeloBlog\\index.html', 'r')
    dados = arquivo.read()
    meuparser1.feed(dados)

meuObjeto()
