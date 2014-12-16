############################################
Subile: Download subtitles from the terminal
############################################

.. image:: https://travis-ci.org/marcwebbie/subile.svg
   :target: https://travis-ci.org/marcwebbie/subile
   :alt: Build status
.. image:: https://coveralls.io/repos/marcwebbie/subile/badge.png
   :target: https://coveralls.io/r/marcwebbie/subile
   :alt: Test Coverage
.. image:: https://pypip.in/version/subile/badge.svg?text=version
   :target: https://pypi.python.org/pypi/subile/
   :alt: Version
.. image:: https://pypip.in/py_versions/subile/badge.svg
   :target: https://pypi.python.org/pypi/subile/
   :alt: Supported Python versions


`Subile <http://github.com/marcwebbie/subile>`_ is a command to download subtitles for videos downloaded videos. Subile supports multiple subtitles languages and provides an interactive interface for choosing the best subtitle.


*******
Install
*******

.. code-block:: bash

    pip install subile


**********
Quickstart
**********

Subile download subtitles with the same name of the video in the same directory with a subtitle extension.

For example for a video called: **~/Videos/hello.world.s01e04.mp4**, the subtitles will be saved into **~/Videos/hello.world.s01e04.srt**

.. code-block:: bash

    # download subtitles for your video in default language "English"
    subile hello.world.s04e10.hdtv.x264-killers.mp4

    # download subtitles for your video in French using `-l fre`
    subile -l fre hello.world.s04e10.hdtv.x264-killers.mp4

    # download subtitles for your video in Portuguese using `-l por`
    subile -l por hello.world.s04e10.hdtv.x264-killers.mp4

    # get into interactive mode using `-i`
    subile -i hello.world.s04e10.hdtv.x264-killers.mp4


******
Issues
******

If you find any issues, please report them on GitHub: `<https://github.com/marcwebbie/subile/issues>`_


************
Contributing
************

Please refer to each project's style guidelines and guidelines for submitting patches and additions.

1. Fork the repo on GitHub: `<https://github.com/marcwebbie/subile/fork>`_
2. Commit changes to a branch in your fork
3. Pull request "upstream" with your changes
4. Merge changes in to "upstream" repo
5. NOTE: Be sure to merge the latest from "upstream" before making a pull request!


*******
License
*******

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
