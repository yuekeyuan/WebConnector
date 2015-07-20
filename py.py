import py2exe
from distutils.core import setup
includes = ["sip","PyQt4.QtGui","PyQt4.QtCore"]

options={"py2exe":{"compressed":1,"optimize":2,"ascii":0,"includes":includes,"bundle_files":0}}

setup(name="hello world", version="1.0.1", description="search panda",
    options= options,zipfile=None,
    windows=[{"script":"main.py","icon_resources":[(1,"a.ico")]}])
