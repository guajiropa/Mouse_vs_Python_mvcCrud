"""
AUTHOR      : Robert James Patterson 
DATE        : 06/03/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial. This is the dialog 
            that will allow the end user to add and modify records
"""
import commonDlgs
import controller
import wx

class AddModRecDialog(wx.Dialog):
    """
    The dialog used to Add / Modify records
    """
    def __init__(self, row=None, title="Add", addRecord=True):
        wx.Dialog.__init__(self, None, title="%s Record" % title)
        self.addRecord = addRecord
        self.selectedRow = row

        if row:
            bTitle = self.selectedRow.title
            fName = self.selectedRow.first_name
            lName = self.selectedRow.last_name
            isbn = self.selectedRow.isbn
            publisher = self.selectedRow.publisher
        else:
            bTitle = fName = lName = isbn = publisher = ""

        size = (80, -1)
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)

        # Create the sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        authorSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create some widgits
        lblNewRec = wx.StaticText(self, label=('%s' % title))
        lblNewRec.SetFont(font)
        mainSizer.Add(lblNewRec, 0, wx.CENTER)

        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        lblTitle = wx.StaticText(self, label="Title:", size=size)
        lblTitle.SetFont(font)
        self.txtTitle = wx.TextCtrl(self, value=bTitle)
        mainSizer.Add(self.rowBuilder([lblTitle, self.txtTitle]), 0, wx.EXPAND)

        lblAuthor = wx.StaticText(self, label="Author:", size=size)
        lblAuthor.SetFont(font)
        authorSizer.Add(lblAuthor, 0, wx.ALL, 5)
        self.txtFirstName = wx.TextCtrl(self, value=fName)
        authorSizer.Add(self.txtFirstName, 1, wx.EXPAND|wx.ALL, 5)
        self.txtLastName = wx.TextCtrl(self, value=lName)
        authorSizer.Add(self.txtLastName, 1, wx.EXPAND|wx.ALL, 5)
        mainSizer.Add(authorSizer, 0, wx.EXPAND)

        lblIsbn = wx.StaticText(self, label="ISBN:", size=size)
        lblIsbn.SetFont(font)
        self.txtIsbn = wx.TextCtrl(self, value=isbn)
        mainSizer.Add(self.rowBuilder([lblIsbn, self.txtIsbn]), 0, wx.EXPAND)

        lblPublisher = wx.StaticText(self, label="Publisher:", size=size)
        lblPublisher.SetFont(font)
        self.txtPublisher = wx.TextCtrl(self, value=publisher)
        mainSizer.Add(self.rowBuilder([lblPublisher, self.txtPublisher]), 0, wx.EXPAND)

        btnOk = wx.Button(self, label="%s" % title)
        btnOk.Bind(wx.EVT_BUTTON, self.onRecord)
        btnSizer.Add(btnOk, 0, wx.ALL, 5)
        btnCancel = wx.Button(self, label="Close")
        btnCancel.Bind(wx.EVT_BUTTON, self.onClose)
        btnSizer.Add(btnCancel, 0, wx.ALL, 5)

        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
    
    def getData(self):
        """
        Method to get the values from the text boxes and store them in a dictionay object.
        """
        dictAuthor = {}
        dictBook = {}

        fName = self.txtFirstName.GetValue()
        lName = self.txtLastName.GetValue()
        title = self.txtTitle.GetValue()
        isbn = self.txtIsbn.GetValue()
        publisher = self.txtPublisher.GetValue()

        if fName == "" or title == "":
            commonDlgs.showMessageDlg("Author and Title are required!", "Error!")
            return

        if "-" in isbn:
            isbn = isbn.replace("-", "_")

        dictAuthor['first_name'] = fName
        dictAuthor['last_name'] = lName
        dictBook['title'] = title
        dictBook['isbn'] = isbn
        dictBook['publisher'] = publisher

        return dictAuthor, dictBook

    def onAdd(self):
        """ 
        Method to add a record to the database.
        """
        dictAuthor, dictBook = self.getData()
        data = ({'author': dictAuthor, 'book': dictBook})
        controller.addRecord(data)

        # display a dialog to notify the end user that the record has been added.
        commonDlgs.showMessageDlg("Book Added!", "Success!", wx.ICON_INFORMATION)

        # clear the text fields to add another record.
        for child in self.GetChildren():
            if isinstance(child, wx.TextCtrl):
                child.SetValue("")
      
    def onEdit(self):
        """ 
        Method to edit data from the database
        """
        dictAuthor, dictBook = self.getData()
        data = ({'author': dictAuthor, 'book': dictBook})
        
        controller.editRecord(self.selectedRow.id, data)
        commonDlgs.showMessageDlg("Edited Successfully!", "Success!", wx.ICON_INFORMATION)
        self.Destroy()

    def onRecord(self, event):
        
        if self.addRecord:
            self.onAdd()
        else:
            self.onEdit()

        self.txtTitle.SetFocus()

    def onClose(self, event):
        """ 
        Cancel the dialog.
        """
        self.Destroy()

    def rowBuilder(self, widgets):
        """ 
        Utility to build label/textbox rows to be added to the sizer
        """
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        lbl, txt = widgets
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(txt, 1, wx.EXPAND|wx.ALL, 5)
        return sizer

#if __name__ == "__main__":
#    app = wx.App(False)
#    dlg = AddModRecDialog()
#    dlg.ShowModal()
#    app.MainLoop()
