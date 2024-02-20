import sys
from pytube import YouTube,Playlist
import moviepy.editor as mp
from arqDir import *
from tqdm import tqdm
import os

class main:
    def __init__(self):
        self.modo = None
        self.nomeDir = "VideosTemp"
        self.nomeDirOut = "Musicas"
        if self.nomeDirOut not in os.listdir():
            os.makedirs(self.nomeDirOut)

    def op(self,modo):
        self.modo = modo

    def executar(self,link):
        try:
            if self.modo == 1:
                playlist = Playlist(link)
                print("Baixando Musicas...")
                for video in tqdm(playlist):
                    self.baixar(video)
            else:
                print("Baixando Musica...")
                self.baixar(link)

            self.toMP3()
            print("\n********* Musicas baixadas e convertidas com sucesso *********\n")
            print("OBS:: As musicas se encontram na pasta Musicas")
        except Exception:
            print("[ON FUNCTION executar] --> Erro ao tentar efetuar a conversão do video")
            return

    def baixar(self,link):
        try:
            youtube = YouTube(link)
            youtube.streams.get_highest_resolution().download(self.nomeDir)
        except Exception:
            print("[ON FUNCTION baixar] --> Erro ao tentar efetuar o download do link")
            return

    def toMP3(self):
        listaVideos = ArqsDir("VideosTemp")
        for video in listaVideos:
            clip = mp.VideoFileClip(self.nomeDir+"/"+video)
            try:
                clip.audio.write_audiofile(self.nomeDirOut+"/"+video[:len(video)-4]+".mp3")
            except Exception:
                print("\n****** Diretorio Musicas não existe, favor criar a pasta para que o algoritmo funcione *******\n")
                return
            clip.close()

        clearDir("VideosTemp")


class interface:
    def __init__(self):
        principal = main()
        while True:
            op = self.menu()
            if op == 1:
                sys.exit(0)
            else:
                op = self.escolherModo()
                if op == 1 or op == 2:
                    principal.op(op)
                    principal.executar(self.lancarLink())

    def menu(self):
        print("\n\t********* menu **********")
        print("\t1 - Sair")
        print("\t2 - Executar algoritmo")
        print("\t-----------------------------")
        op = input("op:: ")
        if op == '1' or op == '2':
            return int(op)
        else:
            print("\n:::::::::: Opção inválida ::::::::::\n")
            return self.menu()

    def escolherModo(self):
        print("\n--------------------------------------------\n")
        print("***** Escolha o modo de download *****")
        print("1- Playlist")
        print("2- Link Unico")
        print("3- Voltar")
        print("\n--------------------------------------------\n")
        op = input("op:: ")
        if op == '1' or op == '2' or op == '3':
            return int(op)
        else:
            print("\n:::::::::: Opção inválida ::::::::::\n")
            return self.escolherModo()

    def lancarLink(self):
        print("\n--------------------------------------------\n")
        link = input("Entre com o link: ")
        print("\n--------------------------------------------\n")
        return link
