from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base   # import the Base from database.py

class Item(Base):
    __tablename__ = "items"   # the actual table name in the DB

    id = Column(Integer, primary_key=True, index=True)   # unique identifier
    name = Column(String, nullable=False, index=True)                # cannot be empty
    description = Column(String, default=None)           # optional text
    price = Column(Float, nullable=False)                # cannot be empty
    is_offer = Column(Boolean, default=False)            # true/false, default False