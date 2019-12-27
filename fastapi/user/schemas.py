from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: str
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str
