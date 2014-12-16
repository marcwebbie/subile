from __future__ import unicode_literals
import argparse
import os

from .fetcher import get_subtitles


def get_args():
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-l", "--language", default='fre',
                         help="subtitles language")
    aparser.add_argument("-o", "--output", action="store_true",
                         help="output filepath")
    aparser.add_argument("-i", "--iteractive", action="store_true",
                         help="iteractive mode")
    aparser.add_argument("video_path",
                         help="path to video for seeking subtitles")
    args = aparser.parse_args()
    return args


def iteractive_choice(subtitles):
    for idx, subtitle in enumerate(subtitles):
        print("[{}] {}".format(idx, subtitle.name))
    subtitle_id = int(input("Subtitles to download : "))
    chosen_subtitle = subtitles[subtitle_id]
    return chosen_subtitle


def run():
    args = get_args()
    video_path = args.video_path
    language = args.language
    subtitles = get_subtitles(video_path, language)

    if subtitles:
        if args.iteractive:
            chosen_subtitle = iteractive_choice(subtitles)
        else:
            chosen_subtitle = next(s for s in subtitles)

        if chosen_subtitle:
            if args.output:
                print(chosen_subtitle.text)
            else:
                basename = os.path.splitext(os.path.basename(video_path))[0]
                subfilename = "{}.{}".format(basename, chosen_subtitle.format)
                with open(subfilename, 'wb') as subfile:
                    subfile.write(chosen_subtitle.content)
                print("Saved subtitles to `{}`".format(subfilename))
        else:
            print("No subtitle were chosen")
    else:
        print("No subtitles were found")


if __name__ == "__main__":
    run()
