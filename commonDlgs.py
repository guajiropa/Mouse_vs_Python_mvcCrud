"""
AUTHOR      : Robert James Patterson (by Mike Driscoll)
DATE        : 05/25/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
import wx

def showMessageDlg(message, caption, flag=wx.ICON_ERROR):
    """ 
    wx.MessageDialog handeler
    """
    msg = wx.MessageDialog(None, message=message, caption=caption, style=flag)
    msg.ShowModal()
    msg.Destroy()
   
