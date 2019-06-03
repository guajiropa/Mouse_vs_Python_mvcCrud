"""
AUTHOR      : Robert James Patterson 
DATE        : 05/27/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
import addModRecord
import commonDlgs
import controller
import wx
from ObjectListView import ObjectListView, ColumnDefn

class BookPanel(wx.Panel):
    """
    This is the main dialog of the application and presents the records from the database in
    the Object List View control.
    """
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        try:
            self.bookResults = controller.getAllRecords()
        except:
            self.bookResults = []
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        
        # create the search related widgets
        cat = ["Author", "Title", "ISBN", "Publisher"]
        searchByLbl = wx.StaticText(self, label="Search By:")
        searchByLbl.SetFont(font)
        searchSizer.Add(searchByLbl, 0, wx.ALL, 5)
        
        self.categories = wx.ComboBox(self, value="Author", choices=cat)
        searchSizer.Add(self.categories, 0, wx.ALL, 5)
        
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
        searchSizer.Add(self.search, 0, wx.ALL, 5)
        
        self.bookResultsOlv = ObjectListView(self, style=wx.LC_REPORT
                                                        |wx.SUNKEN_BORDER)
        self.bookResultsOlv.SetEmptyListMsg("No Records Found")
        self.setBooks()
        
        # create the button row
        btnAddRecord = wx.Button(self, label="Add")
        btnAddRecord.Bind(wx.EVT_BUTTON, self.onAddRecord)
        btnSizer.Add(btnAddRecord, 0, wx.ALL, 5)
        
        btnEditRecord = wx.Button(self, label="Edit")
        btnEditRecord.Bind(wx.EVT_BUTTON, self.onEditRecord)
        btnSizer.Add(btnEditRecord, 0, wx.ALL, 5)
        
        btnDeleteRecord = wx.Button(self, label="Delete")
        btnDeleteRecord.Bind(wx.EVT_BUTTON, self.onDelete)
        btnSizer.Add(btnDeleteRecord, 0, wx.ALL, 5)
        
        btnShowAll = wx.Button(self, label="Show All")
        btnShowAll.Bind(wx.EVT_BUTTON, self.onShowAllRecord)
        btnSizer.Add(btnShowAll, 0, wx.ALL, 5)

        btnClose = wx.Button(self, label="Close")
        btnClose.Bind(wx.EVT_BUTTON, self.onClose)
        btnSizer.Add(btnClose, 0, wx.ALL, 5)
        
        mainSizer.Add(searchSizer)
        mainSizer.Add(self.bookResultsOlv, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)
        
    def onAddRecord(self, event):
        """
        Add a record to the database
        """
        dlg = addModRecord.AddModRecDialog()
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    def onEditRecord(self, event):
        """
        Edit a record
        """
        selectedRow = self.bookResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        dlg = addModRecord.AddModRecDialog(selectedRow, title="Modify",
                                           addRecord=False)
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    def onDelete(self, event):
        """
        Delete a record
        """
        selectedRow = self.bookResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        controller.deleteRecord(selectedRow.id)
        self.showAllRecords()
        
    def onSearch(self, event):
        """
        Searches database based on the user's filter choice and keyword
        """
        filterChoice = self.categories.GetValue()
        keyword = self.search.GetValue()
        print("%s %s" % (filterChoice, keyword))
        self.bookResults = controller.searchRecords(filterChoice, keyword)
        self.setBooks()
        
    def onShowAllRecord(self, event):
        """
        Updates the record list to show all of them
        """
        self.showAllRecords()
        
    def setBooks(self):
        self.bookResultsOlv.SetColumns([
            ColumnDefn("Title", "left", 350, "title"),
            ColumnDefn("Author", "left", 150, "author"),
            ColumnDefn("ISBN", "right", 150, "isbn"),
            ColumnDefn("Publisher", "left", 150, "publisher")
        ])
        self.bookResultsOlv.SetObjects(self.bookResults)
       
    def showAllRecords(self):
        """
        Show all records in the object list view control
        """
        self.bookResults = controller.getAllRecords()
        self.setBooks()
        
    def onClose(self, event):
        """ 
        Exit the app.
        """
        wx.Exit()


class BookFrame(wx.Frame):
    """
    """
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="MvP Media Organizer",
                          size=(800, 600))
        panel = BookPanel(self)
        
        self.Show()
        

#if __name__ == "__main__":
#    app = wx.App(False)
#    frame = BookFrame()
#    app.MainLoop()