"""
AUTHOR      : Robert James Patterson (by Mike Driscoll)
DATE        : 05/25/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
from model import Book, Person, OlvBook
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def addRecord(data):
    """
    The incoming 'data' paramater should be a tuple of two dictionaries in the following 
    format:
    
    ("author":{"first_name":"John", "last_name":"Doe"},
     "book":{"title":"Some book", "isbn":"1234567890", 
             "publisher":"Packt"}
    )
    """
    book = Book()
    book.title = data['book']['title']
    book.isbn = data['book']['isbn']
    book.publisher = data['book']['publisher']
    
    author = Person()
    author.first_name = data['author']['first_name']
    author.last_name = data['author']['last_name']
    book.person = author

    # Create a session, connect to the database, commit and close the connection.
    session = connectToDatabase()
    session.add(book)
    session.commit()
    session.close

def connectToDatabase():
    """ 
    Connect to our SQLite database and return a Session object.
    """
    engine = create_engine('sqlite:///data/bookdata.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def convertResults(results):
    pass

def deleteRecord(idNum):
    pass

def editRecord(idNum, row):
    pass

def getAllRecords():
    pass

def searchRecords(filterChoice, keyword):
    pass


