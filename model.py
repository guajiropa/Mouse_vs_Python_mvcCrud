"""
AUTHOR      : Robert James Patterson (by Mike Driscoll)
DATE        : 06/03/19
SYNOPSIS    : Work thru files for the 'Mouse vs. Python' MVC/CRUD tutorial. This file contains
            the classes that make the tables in the 'bookdata' database. The 
            'metadata.create_all()' statment at the end of this file is the one that will 
            physically create the database file. 
"""
from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation

engine = create_engine('sqlite:///data/bookdata.db', echo=True) 
DeclarativeBase = declarative_base(engine)
metadata = DeclarativeBase.metadata


class OlvBook(object):
    """
    Book model for the ObjectListView
    """
    def __init__(self, id, title, author, isbn, publisher, last_name, first_name):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.last_name = last_name
        self.first_name = first_name


class Person(DeclarativeBase):
    """
    Person model for the 'people' table
    """
    __tablename__ = 'people'

    id = Column(Integer, primary_key = True)
    first_name = Column('first_name', String(50))
    last_name = Column('last_name', String(50))

    def __repr__(self):
        return "<Person : %s %s>" % (self.first_name, self.last_name)


class Book(DeclarativeBase):
    """
    Book model for the 'books' table
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey('people.id'))
    title = Column('title', Unicode)
    isbn = Column('isbn', Unicode)
    publisher = Column('publisher', Unicode)
    person = relation('Person', backref = 'books', cascade_backrefs = False)

    def __repr__(self):
        return "<%s released by %s>" % (str(self.title), str(self.publisher))


#if __name__ == "__main__":
    # Uncomment the line below to create the datadase.
    #metadata.create_all()