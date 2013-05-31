# -*- coding: utf-8 -*-

from setuptools import setup

NAME = 'pyesxi'

VERSION = '1.0.0'

DESCRIPTION = 'ESXi Server control script.'

LONG_DESCRIPTION = """
ESXi Server control script.

Requirements
------------
* Python 2.7


Features
--------
* nonthing


Examples
-------------
VM List.
::

    $ esxi list -H [IPv4 Address of Server] -u [User name] -p [Password]
    
VM powered on.
::

    $ esxi on -H [IPv4 Address of Server] -u [User name] -p [Password] -n [VM name]

Get IPv4 address of VM.(Installed VMware tools)
::

    $ esxi ip -H [IPv4 Address of Server] -u [User name] -p [Password] -n [VM name]

Import OVF or OVA file with file path.
::

    $ esxi import -H [IPv4 Address of Server] -u [User name] -p [Password] --file [OVF or OVA File path] -n [New VM name]

Import OVF or OVA file with file path.(Create mutiple VM)
::

    $ esxi import -H [IPv4 Address of Server] -u [User name] -p [Password] --file [OVF or OVA File path] -n [New VM name1] [New VM name2] ...

Import OVA file with URL.
::

    $ esxi import -H [IPv4 Address of Server] -u [User name] -p [Password] --url [OVA URL] -n [New VM name]


Installation
------------
easy_install:
::

    $ easy_install pyesxi

pip:
::

    $ pip pyesxi


License
-------
Copyright (c) 2013, Kazuki Hasegawa All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

CLASSIFIERS = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Operating System :: OS Independent',
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: BSD License',
    ]

PACKAGES = ['subcommands']

AUTHOR = 'Kazuki Hasegawa'

MAIL_ADDRESS = "hasegawa_0204@hotmail.co.jp"

URL = 'https://github.com/corrupt952/Pyxenter'

LICENSE = 'BSD'

ENTRY_POINTS = """
[console_scripts]
esxi  = esxi:main
"""

REQUIRES = [
    'pysphere',
    ]

KEYWORDS = [
    'ESXi Server',
    ]

setup(name             = NAME,
      version          = VERSION,
      description      = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      classifiers      = CLASSIFIERS,
      packages         = PACKAGES,
      author           = AUTHOR,
      author_email     = MAIL_ADDRESS,
      url              = URL,
      license          = LICENSE,
      entry_points     = ENTRY_POINTS,
      install_requires = REQUIRES,
      )