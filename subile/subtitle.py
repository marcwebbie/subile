from .utils import get_zip_content, lazyproperty


class Subtitle(object):

    def __init__(self, name, format, url, match_ratio):
        self.name = name
        self.format = format
        self.url = url
        self.match_ratio = match_ratio

    @lazyproperty
    def content(self):
        return get_zip_content(self.url)

    @property
    def text(self):
        return self.content.decode('UTF-8', 'ignore')
