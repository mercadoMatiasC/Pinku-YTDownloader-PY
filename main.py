from pytubefix import YouTube
import time
import os

def setup():
    os.system('color d')
    if not os.path.exists('Downloaded Audio'):
        os.makedirs('Downloaded Audio')
    if not os.path.exists('Downloaded Video'):
        os.makedirs('Downloaded Video')

def showDetails(yt):
    print("\n | Title:", yt.title)
    print(" | Author:", yt.author)
    print(" |", yt.length, "seconds\n")

def showStreams(allStreams):
    print(" ----------------------------------------------------------------------")
    for eachStream in allStreams:
            print(" [", eachStream[0], "] - ", eachStream[1].subtype, "\t|  ", eachStream[1].fps, " fps \t| ", eachStream[1].resolution, "  \t|", round(eachStream[1].filesize_approx / 1000000, 2), "Mbs", sep = '')

    print(" [", allStreams[-1][0]+1, "] - Only Audio", sep = '')
    print(" ----------------------------------------------------------------------")

setup()

keepDownloading = True

while(keepDownloading):
    parsed = False
    while(parsed == False):
        os.system('cls')
        print("\n >> Pinku YT Downloader <<\n")
        link = input(" Youtube link: ")
        try:
            yt = YouTube(link)
            showDetails(yt)
            parsed = True
        except:
            input("\n [ That's not a YouTube video link! ]\n Press [ENTER] key to try again...\n ")
    
    allStreams = []

    print(" Getting media...\n")

    for eachFormat in yt.fmt_streams:
        if(eachFormat.subtype == "mp4" and eachFormat.includes_audio_track):
            try:
                eachFormat.fps
            except AttributeError:
                hasFPS = False
            else:
                hasFPS = True

            if(hasFPS):
                allStreams.append(eachFormat)

    allStreams = list(enumerate(allStreams))

    showStreams(allStreams)

    try:
        selected = int(input("\n Select option to download\n Option: "))
    except (ValueError):
        parsed = False
        print(" [ The input option is not listed! ]")
        selected = -1

    while(selected < 0 or selected > allStreams[-1][0]+1):
        os.system('cls')
        print(" [ The input option is not listed! ]")
        showDetails(yt)
        showStreams(allStreams)
        try:
            selected = int(input("\n Select option to download\n Option: "))
        except (ValueError):
            parsed = False
            print(" [ The input option is not listed! ]")

    os.system('color 6')
    print("\n Downloading...\n")

    if(selected == allStreams[-1][0]+1):
        isAudio = True;
        toDownload = yt.streams.filter(only_audio=True).first()
    else:
        isAudio = False;
        toDownload = allStreams[selected][1]

    try:
        if(isAudio):    
            out_file = toDownload.download(output_path="Downloaded Audio")
            base, ext = os.path.splitext(out_file)
            os.rename(out_file, base + ' - PinkuYTD.mp3')
        else:
            out_file = toDownload.download(output_path="Downloaded Video")
            base, ext = os.path.splitext(out_file)
            os.rename(out_file, base + ' - PinkuYTD' + ext)
        print(" [ Downloaded! ]\n")
    except (FileExistsError):
        print(" [ There is already a file downloaded with the same name! ]\n")

    os.system('color d')
    print(" Wanna download anything else?: ")
    if(input(" [1] - Yes\n [Other] - No\n ") != "1"):
        keepDownloading = False

    os.system('cls')

print("\n >> - Thank you for downloading with Pinku YTD - <<")
time.sleep(2)