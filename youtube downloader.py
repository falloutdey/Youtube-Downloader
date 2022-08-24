# Bibliotecas
from pytube import YouTube

# Requisições
print("Bem-vindo(a)!")

opcao = int(input('''
Você deseja:
1 - Baixar video.
2 - Baixar audio.
'''))

url = input('Digite o link do video a ser baixado: ')
video_youtube = YouTube(url)

# Video/Audio Downloader
if opcao == 1:
    resolucao = int(input('''
Você deseja:
1- Baixar video em maior resolução.
2- Baixar video em menor resolução.
'''))
    if resolucao == 1:
        video_youtube.streams.get_highest_resolution().download(output_path = 'YOUTUBE DOWNLOADS VIDEOS')
    
    elif resolucao == 2:
        video_youtube.streams.get_lowest_resolution().download(output_path = 'YOUTUBE DOWNLOADS VIDEOS')
    print('Video baixado!')

elif opcao == 2:
    video_youtube.streams.filter(only_audio = True).first().download(output_path = 'YOUTUBE DOWNLOADS AUDIOS', filename = video_youtube.title + '.mp3')
    print('Audio baixado!')