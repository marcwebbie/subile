import argparse
import os
from difflib import SequenceMatcher

from .utils import get_zip_content
from .subtitles import get_subtitles


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


def run():
    args = get_args()
    video_path = args.video_path
    language = args.language
    subtitles = get_subtitles(video_path, language)
    # print(subtitles)

    if args.iteractive:
        for idx, subtitle in enumerate(subtitles):
            print("[{}] {}".format(idx, subtitle.title))

        chosen_subtitle = subtitles[int(input("Subtitles to download : "))]
    else:
        matcher = lambda x: SequenceMatcher(
            lambda s: None, x.title, args.video_path).ratio()
        subs = sorted(subtitles, key=matcher, reverse=True)
        chosen_subtitle = next((s for s in subs), None)

    if chosen_subtitle:
        download_url = "http://dl.opensubtitles.org/fr/download/sub/{}"
        subtitle_content = get_zip_content(
            download_url.format(chosen_subtitle.id))

        if args.output:
            subtitle_text = subtitle_content.decode('utf-8', 'ignore')
            print(subtitle_text)
        else:
            basename = os.path.splitext(os.path.basename(video_path))[0]
            subfilename = "{}.{}".format(basename, chosen_subtitle.format)
            with open(subfilename, 'wb') as subfile:
                subfile.write(subtitle_content)
            print("Saved {!r} to: `{!r}`".format(chosen_subtitle, subfilename))
    else:
        print("No subtitles were found")


if __name__ == "__main__":
    run()
