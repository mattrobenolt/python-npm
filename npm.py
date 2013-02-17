"""
npm
~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

SITE_PACKAGE = './site-packages'

def init():
    # First, we check to see if a local site-packages exists
    import os
    if not os.path.isdir(SITE_PACKAGES):
        return

    # Found! Insert it onto our path
    import sys
    sys.path.insert(0, SITE_PACKAGES)
    print("site-packages added to path!")


def cli():
    print("hello world")


if __name__ == '__main__':
    init()
