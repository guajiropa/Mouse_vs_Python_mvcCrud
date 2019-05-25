"""
AUTHOR      : Robert James Patterson
DATE        : 05/25/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
import commonDlgs
import controller
import wx


class AddModRecDialog(wx.Dialog):
    """
    The dialog used to Add / Modify records
    """
    def __init__(self, row = None, title = "Add", addRecord = True):
    