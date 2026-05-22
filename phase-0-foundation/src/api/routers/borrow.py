from fastapi import APIRouter , HTTPException ,Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.db import models
from src.schema.borrow import BorrowCreate,BorrowResponse
from src.core.security import get_current_user

from datetime import date

router = APIRouter()

@router.post("/", response_model=BorrowResponse)
def borrow(borrow: BorrowCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    member = db.query(models.Member).filter(models.Member.id == borrow.member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found") # Fixed detail

    # Check if copies are available
    if book.available_copies > 0:
        # ALL code inside the 'if' must be indented
        existing = db.query(models.Borrow).filter(
            models.Borrow.book_id == borrow.book_id,
            models.Borrow.member_id == borrow.member_id,
            models.Borrow.returned_on == None
        ).first()

        if existing:
            raise HTTPException(status_code=400, detail="You have already borrowed this book")
        
        new_borrow = models.Borrow(
            book_id=borrow.book_id,
            member_id=borrow.member_id,
            borrowed_on=date.today()
        )

        book.available_copies -= 1
        db.add(new_borrow)
        db.commit()
        db.refresh(new_borrow)
        return new_borrow

    else:
        # This now correctly matches the 'if book.available_copies > 0'
        raise HTTPException(status_code=400, detail="No copies available for this book")

@router.post("/return/{record_id}", response_model=BorrowResponse)
def return_book(record_id: int, db: Session = Depends(get_db)):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.id == record_id).first()
    if not db_borrow:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    
    if db_borrow.returned_on is not None:
        raise HTTPException(status_code=400, detail="Book already returned")
    
    db_borrow.returned_on = date.today()
    book = db.query(models.Book).filter(models.Book.id == db_borrow.book_id).first()
    
    if book: # Good practice to check if the book still exists
        book.available_copies += 1
        
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

@router.get("/member/{member_id}", response_model=list[BorrowResponse])
def get_borrow_history(member_id: int, db: Session = Depends(get_db)):
    return db.query(models.Borrow).filter(models.Borrow.member_id == member_id).all()