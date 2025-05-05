import datetime
from typing import Optional
import logging

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import get_db

# Use a secure secret key in production (generate via `openssl rand -hex 32`)
SECRET_KEY = "change_this_to_a_random_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


logging.basicConfig(level=logging.DEBUG)

def authenticate_user(db: Session, identifier: str, password: str):
    logging.debug(f"Authenticating user with identifier: {identifier}")
    user = crud.get_user_by_identifier(db, identifier)
    if not user:
        logging.debug("User not found")
        return False
    if not verify_password(password, user.password_hash):
        logging.debug("Invalid password")
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + (
        expires_delta if expires_delta else datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    # Lookup the user by login prefix & ID, without re-verifying password
    login = token_data.username
    if login.startswith("student-"):
        role = "student"
        id_val = login[len("student-"):]
        user = db.query(models.User).filter(models.User.role == role, models.User.student_id == id_val).first()
    elif login.startswith("fac-"):
        role = "faculty"
        id_val = login[len("fac-"):]
        user = db.query(models.User).filter(models.User.role == role, models.User.faculty_id == id_val).first()
    elif login.startswith("adm-"):
        role = "admin"
        id_val = login[len("adm-"):]
        user = db.query(models.User).filter(models.User.role == role, models.User.admin_id == id_val).first()
    else:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user 