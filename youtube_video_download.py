from pytube import YouTube


def download(link):

    try:
        youtubeobject = YouTube(link)
        resolution = youtubeobject.streams.get_highest_resolution()
        resolution.download()

    except:
        print('Error!!!!!!')

    print('download Completed!!!')

download()
