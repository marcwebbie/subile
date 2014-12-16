from __future__ import unicode_literals
from difflib import SequenceMatcher

from pyquery import PyQuery
from .utils import session
from .subtitle import Subtitle


def build_search_params(subtitle_language, **info):
    title = info.get("series", info.get("title"))
    is_tvshow = info.get("type") == "episode"
    season = info.get("season", "")
    episode = info.get("episodeNumber", "")
    params = {
        "MovieName": title,
        "id": 8,
        "action": "search",
        "SubLanguageID": subtitle_language,
        "SearchOnlyTVSeries": "on" if is_tvshow else "",
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
        "MovieYear": info.get('year', ""),
        "MovieFPS": "",
        "SubFormat": "",
        "SubAddDate": "",
        "Uploader": "",
        "IDUser": "",
        "IMDBID": info.get('imdbid', ""),
        "IDMovie": "",
        "MovieHash": info.get('movie_hash', ""),
    }

    return params


def match_ratio(title, filename):
    return SequenceMatcher(None, title, filename).ratio()


def fetch(language, video_info):
    api_url = "http://www.opensubtitles.org/fr/search2"
    params = build_search_params(language, **video_info)
    res = session.get(api_url, params=params)
    pq = PyQuery(res.content)

    subtitles = []
    elems = pq('table#search_results>tbody>tr[onclick]')
    for elem in elems.items():
        sub_id = elem.attr('id').replace('name', '')
        sub_url = "http://dl.opensubtitles.org/fr/download/sub/{}".format(
            sub_id
        )
        sub_title = elem('td[id^="main"]>strong>a').attr('title').replace(
            'sous-titres - ', '')
        name_elem = elem('td[id^="main"]>span[title]')
        sub_name = sub_title if not name_elem else name_elem.attr("title")
        sub_format = elem('.p:last').html()
        sub_match_ratio = match_ratio(sub_name, video_info['filename'])

        subtitle = Subtitle(sub_name, sub_format, sub_url, sub_match_ratio)
        subtitles.append(subtitle)

    return sorted(subtitles, key=lambda x: x.match_ratio, reverse=True)
