from plus import usage1
import cloudmusic

if __name__ == '__main__':

    playlist_id = 8134828337

    playlist = cloudmusic.getPlaylist(playlist_id)
    for music in playlist:
        usage1.download(music)
