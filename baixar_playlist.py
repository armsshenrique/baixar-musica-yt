"""
Necessario instalar: 
pip install pytube 
pip install moviepy
"""

from moviepy.video.io.VideoFileClip import AudioFileClip
from os import remove
import pytube


def downloadPlaylist(url):
    playlist = pytube.Playlist(url)

    for video in playlist.videos:
        videobaixado = video.streams.get_audio_only().download()

        arquivomp3 = AudioFileClip(videobaixado)
        arquivomp3.write_audiofile(videobaixado[:-4] + ".mp3")
        arquivomp3.close()
        remove(videobaixado)


downloadPlaylist(
    'https://www.youtube.com/playlist?list=PLsedSoXEihT4kPOHUhPVO0IJlmyfqJ0S6')
