"""
AUTHOR      : Robert James Patterson 
DATE        : 06/23/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial. This file is the heart
            of the appliction and handles the interactions with the database.
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
    # Create an instance of the Book and Person classes and populate them with the values
    # collected from the 'Add' dialog and passed in as the tuple of dictionaries.
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

def editRecord(idNum, data):
    """
    Edit a record and save changes to the database. The 'idNum' parameter is the id of the 
    record to edit. The incoming 'data' parameter is again, a tuple of two dictionaries.
    """
    # Create a session, query the database for the 'Book' record with the same 'Id' key
    # and a create a record object holding that record.
    session = connectToDatabase()
    record = session.query(Book).filter_by(id=idNum).one()
    
    # Update the fields in the record with the values that were passed in.
    record.title = data['book']['title']
    record.person.first_name = data['author']['first_name']
    record.person.last_name = data['author']['last_name']
    record.isbn = data['book']['isbn']
    record.publisher = data['book']['publisher']

    # Save to database and close connection.
    session.add(record)
    session.commit()
    session.close()

def deleteRecord(idNum):
    """ 
    Delete a record from the database
    """
    session = connectToDatabase()
    record = session.query(Book).filter_by(id=idNum).one()
    session.delete(record)
    session.commit()
    session.close()

def convertResults(results):
    """
    Format the 'results' for the OlvBooks objects and return it as a list
    """
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

def getAllRecords():
    """ 
    Get all of the records and return them.
    """
    session = connectToDatabase()
    result = session.query(Book).all()
    books = convertResults(result)
    session.close()

    return books

def searchRecords(filterChoice, keyword):
    """ 
    Search based on an end user provieded keyword.
    """
    session = connectToDatabase()
    if filterChoice == 'Author':
        qry = session.query(Person)
        result = qry.filter(Person.first_name.contains('%s' % keyword)).all()
        records = []
        for record in result:
            for book in record.books:
                records.append(book)

        result = records

    elif filterChoice == 'Title':
        qry = session.query(Book)
        result = qry.filter(Book.title.contains('%s' % keyword)).all()
    elif filterChoice == "ISBN":
        qry = session.query(Book)
        result = qry.filter(Book.isbn.contains('%s' % keyword)).all()
    else:
        qry = session.query(Book)
        result = qry.filter(Book.publisher.contains('%s' % keyword)).all()    
    books = convertResults(result)
    return books