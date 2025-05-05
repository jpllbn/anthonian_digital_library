from sqlalchemy import Column, Integer, String, Text, Enum, Boolean, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(Enum('student', 'faculty', 'admin'), nullable=False)
    identifier = Column(String(30), unique=True, nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, nullable=False)

class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_title = Column(String(100), nullable=False)
    category_id = Column(Integer, nullable=False)
    author = Column(String(50), nullable=False)
    book_copies = Column(Integer, nullable=False)
    book_pub = Column(String(100), nullable=False)
    publisher_name = Column(String(100), nullable=False)
    isbn = Column(String(50), nullable=False)
    copyright_year = Column(Integer, nullable=False)
    date_receive = Column(String(20), nullable=False)
    date_added = Column(TIMESTAMP, nullable=False)
    status = Column(String(30), nullable=False)

class Borrow(Base):
    __tablename__ = "borrow"

    borrow_id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, nullable=False)
    date_borrow = Column(String(100), nullable=False)
    due_date = Column(String(100))

class BorrowDetails(Base):
    __tablename__ = "borrowdetails"

    borrow_details_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, nullable=False)
    borrow_id = Column(Integer, nullable=False)
    borrow_status = Column(String(50), nullable=False)
    date_return = Column(String(100), nullable=False)

class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    classname = Column(String(50))

class LostBook(Base):
    __tablename__ = "lost_book"

    Book_ID = Column(Integer, primary_key=True, autoincrement=True)
    ISBN = Column(Integer, nullable=False)
    Member_No = Column(String(50), nullable=False)
    Date_Lost = Column(TIMESTAMP, nullable=False)

class Member(Base):
    __tablename__ = "member"

    member_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    address = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    year_level = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    borrowertype = Column(String(50)) 