from pytube import YouTube
import os
from os import system, name

# https://youtu.be/n78Gg6_zEQg
while True:
    try:
        print("""
        ███╗   ███╗███████╗████████╗██╗   ██╗██████╗ ███████╗    ██╗   ██╗ ██████╗    ██╗
        ████╗ ████║██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██║   ██║██╔═████╗  ███║
        ██╔████╔██║█████╗     ██║   ██║   ██║██████╔╝█████╗      ██║   ██║██║██╔██║  ╚██║
        ██║╚██╔╝██║██╔══╝     ██║   ██║   ██║██╔══██╗██╔══╝      ╚██╗ ██╔╝████╔╝██║   ██║
        ██║ ╚═╝ ██║███████╗   ██║   ╚██████╔╝██████╔╝███████╗     ╚████╔╝ ╚██████╔╝██╗██║
        ╚═╝     ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝      ╚═══╝   ╚═════╝ ╚═╝╚═╝
                                Dev : D O R T R O 乂\n\n""")
        link = input('Paste youtube video video link:\n')

        while True:
            try:
                video_audio = int(input("\nPress 1 for Video\nPress 2 for audio\n"))
                if video_audio <= 2 and video_audio > 0:
                    break
                print("Invalid input.")
            except Exception as e:
                print(e)

        while video_audio == 1:
            destination = "./Video Downloads"
            try:
                quality = int(input("Press 1 for 720p\nPress 2 for 480p\nPress 3 for 360p\nPress 4 for 144p\n"))
                if quality <= 4 and quality > 0:
                    if quality == 1:
                        tag = 136
                        break
                    elif quality == 2:
                        tag = 135
                        break
                    elif quality == 3:
                        tag = 134
                        break
                    elif quality == 4:
                        tag = 160
                        break
                print("Invalid input.")
            except Exception as e:
                print(e)

        while video_audio == 2:
            destination = "./Audio Downloads"
            try:
                quality = int(input("Press 1 for 120kbps\nPress 2 for 160kbps\n"))
                if quality <= 4 and quality > 0:
                    if quality == 1:
                        tag = 140
                        break
                    elif quality == 2:
                        tag = 251
                        break
                print("Invalid input.")
            except Exception as e:
                print(e)

        print(f"tag {tag}")    

        yt = YouTube(link)
        print(f"Downloading : {yt.title}\nwill be added shortly...")
        stream = yt.streams.get_by_itag(tag)
        ogdes = stream.download(output_path=destination)
        if video_audio == 2:
            base, ext = os.path.splitext(ogdes)
            newdes = base + '.mp3'
            os.rename(ogdes, newdes)
        else:
            pass
        print("Successfully downloaded")
        while True:
            try:
                loop = input("Want to download next song?\n[y/n]: ").lower()
                if loop == "n" or loop == "y":
                    break
                print("Invalid input!")
            except Exception as e:
                print(e)
        if loop == "n":
            break
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    except Exception as e:
        print(e)