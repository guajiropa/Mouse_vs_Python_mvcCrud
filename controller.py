"""
AUTHOR      : Robert James Patterson (by Mike Driscoll)
DATE        : 05/26/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial.
"""
from model import Book, Person, OlvBook
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connectToDatabase():
    """ 
    Connect to our SQLite database and return a Session object.
    """
    engine = create_engine('sqlite:///data/bookdata.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

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

def convertResults(results):
    """
    Format the 'results' for the OlvBooks objects and return it as a list
    """

    # this print statement is here for debugging
    print

    books = []
    for record in results:
        author = "%s %s" % (record.person.first_name, record.person.last_name)
        book = OlvBook(record.id,
                       record.title,
                       author,
                       record.isbn,
                       record.publisher,
                       record.person.last_name,
                       record.person.first_name
                       )
        books.append(book)
    return books

def deleteRecord(idNum):
    """ 
    Delete a record from the database
    """
    session = connectToDatabase()
    record = session.query(Book).filter_by(id=idNum).one()
    session.delete(record)
    session.commit()
    session.close()

def editRecord(idNum, row):
    """
    Edit a record and save changes to the database.
    """
    session = connectToDatabase()
    record = session.query(Book).filter_by(id=idNum).one()
    print
    record.title = row['title']
    record.person.first_name = row['first_name']
    record.person.last_name = row['last_name']
    record.isbn = row['isbn']
    record.publisher = row['publisher']

    session.add(record)
    session.commit()
    session.close()

def getAllRecords():
    """ 
    Get all of the records and return them.
    """


def searchRecords(filterChoice, keyword):
    pass


