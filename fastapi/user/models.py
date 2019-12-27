from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from main.database import Base


class UserModel(Base):
    __tablename__ = 'user_users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    # items = relationship("Item", back_populates="owner")
