"""
Necessario instalar: 
pip install pytube 
pip install moviepy
"""
from moviepy.video.io.VideoFileClip import AudioFileClip
from tkinter import filedialog
from pytube import YouTube
from os import remove


def BaixarAudio(url):
    video = YouTube(url)
    dirpath = filedialog.askdirectory()
    diretorio = dirpath
    videobaixado = video.streams.get_audio_only().download(diretorio)
    arquivomp3 = AudioFileClip(videobaixado)
    arquivomp3.write_audiofile(videobaixado[:-4] + ".mp3")
    arquivomp3.close()
    remove(videobaixado)


BaixarAudio(input('Digite o url do video: '))
print('Selecione a pasta para salva a musica ....')
