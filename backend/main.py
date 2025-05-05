from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app import models, crud, schemas
from app.database import engine, Base, get_db
from app.auth import authenticate_user, create_access_token, get_current_active_user

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Anthonian Library Auth API")

# Add CORS middleware so the frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check for existing username or email
    if crud.get_user(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Use identifier instead of username
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect identifier or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.identifier})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user

# Book Endpoints

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/books/", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

# Borrow Endpoints

@app.get("/borrows/{borrow_id}", response_model=schemas.Borrow)
def read_borrow(borrow_id: int, db: Session = Depends(get_db)):
    db_borrow = crud.get_borrow(db, borrow_id=borrow_id)
    if db_borrow is None:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    return db_borrow

@app.post("/borrows/", response_model=schemas.Borrow, status_code=status.HTTP_201_CREATED)
def create_borrow(borrow: schemas.BorrowCreate, db: Session = Depends(get_db)):
    return crud.create_borrow(db=db, borrow=borrow)

# BorrowDetails Endpoints

@app.get("/borrowdetails/{borrow_details_id}", response_model=schemas.BorrowDetails)
def read_borrow_details(borrow_details_id: int, db: Session = Depends(get_db)):
    db_borrow_details = crud.get_borrow_details(db, borrow_details_id=borrow_details_id)
    if db_borrow_details is None:
        raise HTTPException(status_code=404, detail="Borrow details not found")
    return db_borrow_details

@app.post("/borrowdetails/", response_model=schemas.BorrowDetails, status_code=status.HTTP_201_CREATED)
def create_borrow_details(borrow_details: schemas.BorrowDetailsCreate, db: Session = Depends(get_db)):
    return crud.create_borrow_details(db=db, borrow_details=borrow_details)

# Category Endpoints

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.post("/categories/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# LostBook Endpoints

@app.get("/lostbooks/{book_id}", response_model=schemas.LostBook)
def read_lost_book(book_id: int, db: Session = Depends(get_db)):
    db_lost_book = crud.get_lost_book(db, book_id=book_id)
    if db_lost_book is None:
        raise HTTPException(status_code=404, detail="Lost book not found")
    return db_lost_book

@app.post("/lostbooks/", response_model=schemas.LostBook, status_code=status.HTTP_201_CREATED)
def create_lost_book(lost_book: schemas.LostBookCreate, db: Session = Depends(get_db)):
    return crud.create_lost_book(db=db, lost_book=lost_book)

# Member Endpoints

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.post("/members/", response_model=schemas.Member, status_code=status.HTTP_201_CREATED)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

# Type Endpoints

@app.get("/types/{type_id}", response_model=schemas.Type)
def read_type(type_id: int, db: Session = Depends(get_db)):
    db_type = crud.get_type(db, type_id=type_id)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_type

@app.post("/types/", response_model=schemas.Type, status_code=status.HTTP_201_CREATED)
def create_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    return crud.create_type(db=db, type=type) 