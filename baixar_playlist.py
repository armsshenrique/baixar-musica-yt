"""
Necessario instalar: 
pip install pytube 
pip install moviepy
"""

from moviepy.video.io.VideoFileClip import AudioFileClip
from tkinter import filedialog
from os import remove
import pytube


def downloadPlaylist(url):
    playlist = pytube.Playlist(url)
    dirpath = filedialog.askdirectory()
    diretorio = dirpath
    print('Selecione a pasta para salvar as musicas ....')

    for video in playlist.videos:
        videobaixado = video.streams.get_audio_only().download(diretorio)

        arquivomp3 = AudioFileClip(videobaixado)
        arquivomp3.write_audiofile(videobaixado[:-4] + ".mp3")
        arquivomp3.close()
        remove(videobaixado)


downloadPlaylist(input('Digite o url da PLAYLIST: '))
