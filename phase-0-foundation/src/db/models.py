from sqlalchemy import Column,Integer,String,Float,Enum,ForeignKey,Date
from src.db.database import Base 
import enum

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer,primary_key =True,index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    total_copies = Column(Integer)
    available_copies = Column(Integer)

class MembershipType(str, enum.Enum):
    basic = "basic"
    premium = "premium"

class Member(Base):
    __tablename__ = "member"

    id = Column(Integer,primary_key =True,index=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String,nullable=False)
    phone = Column(String)
    membership_type = Column(Enum(MembershipType,name="membership_type")) 

class Borrow(Base):
    __tablename__ = "borrow"

    id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("book.id"))
    member_id = Column(Integer,ForeignKey("member.id"))
    borrowed_on = Column(Date)
    returned_on = Column(Date,nullable=True)

class Product(Base):

    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float) 
    quantity = Column(Integer)
