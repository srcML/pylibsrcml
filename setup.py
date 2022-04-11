 #############################################################################
 # @file setup.py
 #
 # @copyright Copyright (C) 2018-2019 srcML, LLC. (www.srcML.org)
 #
 # This file is part of the srcML Toolkit.
 #
 # The srcML Toolkit is free software; you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation; either version 2 of the License, or
 # (at your option) any later version.
 #
 # The srcML Toolkit is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 # You should have received a copy of the GNU General Public License
 # along with the srcML Toolkit; if not, write to the Free Software
 # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 #############################################################################

import setuptools

setuptools.setup(
    name = 'pylibsrcml',
    version = '1.0.0',
    author = 'srcML Team',
    author_email = 'srcml@kent.edu',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    py_modules = ['libsrcml'],
    url = 'https://www.srcml.org/',
    license = 'LICENSE.txt',
    description = 'A set of Python bindings for srcML.',
    long_description = open('README.md').read(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License V3",
        "Operating System :: OS Independent",
    ]
)
