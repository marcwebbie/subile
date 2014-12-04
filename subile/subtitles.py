# -*- coding: utf-8 -*-
import os
import sys
import re
from collections import namedtuple

import guessit
from pyquery import PyQuery

from utils import session


Subtitle = namedtuple("Subtitle", "id title format")


def get_subtitles(video_path, language, *args, **kwargs):
    """
    Go to opensubtitles and download w
    """

    video_path = os.path.basename(os.path.abspath(video_path))
    guessit.patterns.basestring = str  # Patch ugly code
    info = guessit.guess_episode_info(video_path)

    try:
        show = info['series']
        season = info['season']
        episode = info['episodeNumber']
    except KeyError:
        print("Couldn't guess video info from file: {}".format(video_path))
        sys.exit(1)

    api_url = "http://www.opensubtitles.org/fr/search2"

    params = {
        "MovieName": show,
        "id": 8,
        "action": "search",
        "SubLanguageID": language,
        "SubLanguageID": language,
        "SearchOnlyTVSeries": "on",
        "Season": season,
        "Episode": episode,
        "SubSumCD": 1,
        "Genre": "",
        "MovieByteSize": "",
        "MovieLanguage": "",
        "MovieImdbRatingSign": 1,
        "MovieImdbRating": "",
        "MovieCountry": "",
        "MovieYearSign": 1,
        "MovieYear": kwargs.get('year', ""),
        "MovieFPS": "",
        "SubFormat": "",
        "SubAddDate": "",
        "Uploader": "",
        "IDUser": "",
        "IMDBID": kwargs.get('imdbid', ""),
        "IDMovie": "",
        "MovieHash": kwargs.get('movie_hash', ""),
    }

    res = session.get(api_url, params=params)
    pq = PyQuery(res.content)

    subtitles = []
    for elem in pq('table#search_results tr[id^="name"]').items():
        sub_id = elem.attr('id').replace('name', '')
        sub_format = elem('.p:last').text()
        elem('td:first a').remove()
        elem('td:first img').remove()
        elem('td:first strong').remove()
        sub_title = re.sub(r'\[.*?\]\s+', '', elem('td:first').text())

        sub = Subtitle(id=sub_id, title=sub_title, format=sub_format)
        subtitles.append(sub)

    return subtitles
