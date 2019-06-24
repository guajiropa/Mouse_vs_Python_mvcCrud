"""
AUTHOR      : Robert James Patterson
DATE        : 06/23/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial. This tutorial 
            was written using Python 2.5 and did not function correctly in Python 3. 
            Rewrote the code and got it running on Python 3.5
"""
from wx import App
from mainView import BookFrame

if __name__ == "__main__":
    app = App(False)
    frame = BookFrame()
    app.MainLoop()