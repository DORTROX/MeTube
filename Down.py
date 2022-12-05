from pytube import YouTube, Playlist
import os
from os import system, name

def playlistSongs (url, destination):
    try:
        yt = YouTube(url)
        contentA = yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(contentA[4].itag)
        ogdes = stream.download(output_path=destination)
        base, ext = os.path.splitext(ogdes)
        newdes = base + '.mp3'
        os.rename(ogdes, newdes)
    except Exception as e:
        print(e)


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
        if "playlist?list=" in link:
            try:
                print("Found Playlist\n")
                destination = input("Enter a name for the playlist : ")
                print("Downloading your Playlist for you be patient\n")
                cwd = os.getcwd()
                target_dir = cwd +'/' + destination;
                os.mkdir(target_dir)
                p = Playlist(link)
                for url in p.video_urls:
                    playlistSongs(url, './' + destination)
                print("Download Complete!")
            except Exception as e:
                print(e)
        else:
            yt = YouTube(link)
            while True:
                try:
                    video_audio = int(input("\nPress 1 for Video\nPress 2 for audio\n"))
                    if video_audio <= 2 and video_audio > 0:
                        break
                    print("Invalid input.")
                except Exception as e:
                    print(e)

            while video_audio == 1:
                contentV = yt.streams.filter(progressive=True)
                i = 0
                for avail in contentV:
                    i+=1
                    print(f"Press {i} for {avail.resolution}")

                destination = "./Video Downloads"
                try:
                    quality = int(input("Enter No.: "))
                    if i ==  2:
                        if quality <= i and quality > 0:
                            if quality == 1:
                                tag = contentV[0].itag
                                break
                            elif quality == 2:
                                tag = contentV[1].itag
                                break
                        print("Invalid")
                    else:
                        if quality <= i and quality > 0:
                            if quality == 1:
                                tag = contentV[0].itag
                                break
                            elif quality == 2:
                                tag = contentV[1].itag
                                break
                            elif quality == 3:
                                tag = contentV[2].itag
                                break
                        print("Invalid")
                except Exception as e:
                    print(e)

            while video_audio == 2:
                contentA = yt.streams.filter(only_audio=True)

                i = 0
                for avail in contentA:
                    i+=1
                    print(f"Press {i} for {avail.abr}")
                destination = "./Audio Downloads"
                try:
                    quality = int(input("Enter No.: "))
                    if quality <= i and quality > 0:
                        if quality == 1:
                            tag = contentA[0].itag
                            break
                        elif quality == 2:
                            tag = contentA[1].itag
                            break
                        elif quality == 3:
                            tag = contentA[2].itag
                            break
                        elif quality == 4:
                            tag = contentA[3].itag
                            break
                        elif quality == 5:
                            tag = contentA[4].itag
                            break
                    print("Invalid input.")
                except Exception as e:
                    print(e)
        
        # while video_audio ==  3: 
        #     contentP = input("Enter the Playlist URL here")

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
                loop = input("Want to download next Video/Audio?\n[y/n]: ").lower()
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