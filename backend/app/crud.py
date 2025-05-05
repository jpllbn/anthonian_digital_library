from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash


def get_user(db: Session, username: str):
    """Retrieve a user by username."""
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    """Retrieve a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_identifier(db: Session, identifier: str):
    return db.query(models.User).filter(models.User.identifier == identifier).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user with hashed password."""
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed_password,
        role=user.role,
        identifier=user.identifier,
        is_verified=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Book CRUD operations

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Borrow CRUD operations

def get_borrow(db: Session, borrow_id: int):
    return db.query(models.Borrow).filter(models.Borrow.borrow_id == borrow_id).first()


def create_borrow(db: Session, borrow: schemas.BorrowCreate):
    db_borrow = models.Borrow(**borrow.dict())
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow


# BorrowDetails CRUD operations

def get_borrow_details(db: Session, borrow_details_id: int):
    return db.query(models.BorrowDetails).filter(models.BorrowDetails.borrow_details_id == borrow_details_id).first()


def create_borrow_details(db: Session, borrow_details: schemas.BorrowDetailsCreate):
    db_borrow_details = models.BorrowDetails(**borrow_details.dict())
    db.add(db_borrow_details)
    db.commit()
    db.refresh(db_borrow_details)
    return db_borrow_details


# Category CRUD operations

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.category_id == category_id).first()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# LostBook CRUD operations

def get_lost_book(db: Session, book_id: int):
    return db.query(models.LostBook).filter(models.LostBook.Book_ID == book_id).first()


def create_lost_book(db: Session, lost_book: schemas.LostBookCreate):
    db_lost_book = models.LostBook(**lost_book.dict())
    db.add(db_lost_book)
    db.commit()
    db.refresh(db_lost_book)
    return db_lost_book


# Member CRUD operations

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.member_id == member_id).first()


def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


# Type CRUD operations

def get_type(db: Session, type_id: int):
    return db.query(models.Type).filter(models.Type.id == type_id).first()


def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Type(**type.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type 