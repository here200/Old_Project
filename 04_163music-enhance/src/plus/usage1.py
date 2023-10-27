import os
import re


def output_info(music):
    print("歌名：{}, 歌手：{}, 音频文件url：{}".format(music.name, music.artist, music.url))


def download(music, save_dir="./cloudmusic/", foo=None):
    if not os.path.exists(save_dir):  # 第一次执行
        _execute(music, save_dir, foo)
    else:  # 避免重复下载
        if not _is_exist(music, save_dir):
            _execute(music, save_dir, foo)
        else:
            print("====={} 已存在，不再重新下载=====".format(music.name))


def _is_exist(music, save_dir):
    # 生成正则表达式（参考实现）
    if len(music.artist) == 1:
        artist = music.artist[0]
    else:
        artist = " ".join(music.artist)
    regex = ("{}.*?{}".format(music.name, artist)).replace("(", ".").replace(")", ".")

    return len(re.findall(regex, " ".join(os.listdir(save_dir)))) != 0


def _execute(music, save_dir, foo=None):
    print("====={} 正在下载=====".format(music.name))

    if foo:
        foo()
    else:
        music.download(dirs=save_dir, level="lossless")
