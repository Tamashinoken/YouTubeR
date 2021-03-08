'''
Ushbu dastur YouTube saytidan videolarni turli sifatda ko`chirib olish imkonini beradi
Muallif: Ashurov Sindor
Versiya: 1.0.0
'''

import pytube 

# YouTube saytiga kirib, o`zimizga kerakli videoni topamiz
# Keyin uning linkidan nusxa olamiz
# Terminal orqali python YouTubeR.py deb yozamiz

url = input('YouTube dan yuklab olmoqchi bo`lgan videoning linkini kiriting:')

y = pytube.YouTube(url)
v = int(input(''' Videoning sifatini tanlang:

1 - o`rtacha
2 - eng yuqori sifatli

'''))

if (v == 1):
    video = youtube.streams.first()
    video.download()
elif (v == 2):
    video = y.streams.get_highest_resolution().download()

else:
    print('Siz noto`g`ri qiymat kiritdingiz!')
