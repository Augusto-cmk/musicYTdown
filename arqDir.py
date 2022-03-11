import os

def clearDir(nomeDiretorio):
    listaArquivos = ArqsDir(nomeDiretorio)
    for arquivo in listaArquivos:
        os.remove(nomeDiretorio+"/"+arquivo)

def ArqsDir(nomeDiretorio):
    try:
        return os.listdir(nomeDiretorio)
    except Exception:
        print("\n[ON arqDir at function ArqsDir] --> Diretorio não encontrado\n")


