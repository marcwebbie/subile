# -*- coding: utf-8 -*-
import os

import guessit
from . import opensubtitles


def get_video_info(video_path):
    video_path = os.path.abspath(video_path)
    video_name = os.path.basename(video_path)
    video_info = guessit.guess_video_info(video_name)
    video_info["filename"] = os.path.splitext(video_name)[0]
    return video_info


def get_subtitles(video_path, language):
    video_info = get_video_info(video_path)
    subtitles = opensubtitles.fetch(language, video_info)
    return subtitles
