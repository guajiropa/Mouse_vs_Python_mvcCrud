"""
AUTHOR      : Robert James Patterson
DATE        : 06/03/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
from wx import App
from mainView import BookFrame

if __name__ == "__main__":
    app = App(False)
    frame = BookFrame()
    app.MainLoop()