#!/usr/bin/env python
"""
npm
~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

from distutils.core import setup
from distutils.command.install_data import install_data


class install_sitepackages(install_data):
    def finalize_options(self):
        self.warn_dir = 0
        self.install_dir = self.get_finalized_command('install').install_lib
        install_data.finalize_options(self)

setup(
    name='npm',
    version='0.0.1',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/python-npm',
    license='BSD',
    description='npm',
    long_description=__doc__,
    author='Matt Robenolt',
    py_modules=['npm'],
    data_files=['npm.pth'],
    cmdclass={'install_data': install_sitepackages},
    entry_points={'console_scripts': ['npmpy = npm:cli']},
    zip_safe=False,
    classifiers=[],
)
