"""
AUTHOR      : Robert James Patterson (by Mike Driscoll)
DATE        : 05/25/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
# ------------------------------------------------------------
# mediaLocker.py
#
# Author: Mike Driscoll
# Contact: mike@pythonlibrary.org
#
# This program demonstrates how to work with a SQLite database
# using wxPython and SqlAlchemy. It is also an example of MVC
# concepts and how to put together a fully working wxPython
# application.
# ------------------------------------------------------------
from wx import App
from mainView import BookFrame

if __name__ == "__main__":
    app = App(False)
    frame = BookFrame()
    app.MainLoop()