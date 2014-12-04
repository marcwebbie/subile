import os
import zipfile

import requests
try:
    from io import BytesIO
except:
    # python2
    from StringIO import StringIO as BytesIO


headers = {
    "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/32.0.1674.0 Safari/537.36")
}
session = requests.Session()
session.headers.update(headers)
http_adapter = requests.adapters.HTTPAdapter(
    pool_connections=100, pool_maxsize=100)
session.mount('http://', http_adapter)


def get_zip_content(download_url):
    zip_response = session.get(download_url)
    zfile = zipfile.ZipFile(BytesIO(zip_response.content))

    FORMATS = (".sub", ".srt", ".idx", ".ass")
    for sub_name in (name for name in zfile.namelist()
                     if os.path.splitext(name)[-1] in FORMATS):
        return zfile.read(sub_name)
    else:
        return None
