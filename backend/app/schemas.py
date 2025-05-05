from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: str
    identifier: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class BookBase(BaseModel):
    book_title: str
    category_id: int
    author: str
    book_copies: int
    book_pub: str
    publisher_name: str
    isbn: str
    copyright_year: int
    date_receive: str
    date_added: datetime
    status: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    book_id: int

    class Config:
        from_attributes = True


class BorrowBase(BaseModel):
    member_id: int
    date_borrow: str
    due_date: Optional[str]


class BorrowCreate(BorrowBase):
    pass


class Borrow(BorrowBase):
    borrow_id: int

    class Config:
        from_attributes = True


class BorrowDetailsBase(BaseModel):
    book_id: int
    borrow_id: int
    borrow_status: str
    date_return: str


class BorrowDetailsCreate(BorrowDetailsBase):
    pass


class BorrowDetails(BorrowDetailsBase):
    borrow_details_id: int

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    classname: Optional[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    category_id: int

    class Config:
        from_attributes = True


class LostBookBase(BaseModel):
    ISBN: int
    Member_No: str
    Date_Lost: datetime


class LostBookCreate(LostBookBase):
    pass


class LostBook(LostBookBase):
    Book_ID: int

    class Config:
        from_attributes = True


class MemberBase(BaseModel):
    firstname: str
    lastname: str
    gender: str
    address: str
    contact: str
    type: str
    year_level: str
    status: str


class MemberCreate(MemberBase):
    pass


class Member(MemberBase):
    member_id: int

    class Config:
        from_attributes = True


class TypeBase(BaseModel):
    borrowertype: Optional[str]


class TypeCreate(TypeBase):
    pass


class Type(TypeBase):
    id: int

    class Config:
        from_attributes = True 