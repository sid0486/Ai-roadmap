from fastapi import APIRouter , HTTPException ,Depends
from sqlalchemy.orm import Session 
from src.db.database import get_db
from src.schema.books import BookCreate , BookResponse
from src.db import models 

router = APIRouter()

@router.get("/",response_model=list[BookResponse])
def get_all_books(db:Session=Depends(get_db)):
    return db.query(models.Book).order_by(models.Book.id).all()

@router.get("/{id}",response_model=BookResponse)
def get_by_id(id:int,db:Session=Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found")
    return db_book

@router.post("/",response_model=BookResponse)
def add_book(book:BookCreate,db:Session=Depends(get_db)):
    existing = db.query(models.Book).filter(models.Book.title==book.title).first()
    if existing:
        raise HTTPException(status_code=400,detail="Book already exists")
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{id}",response_model=BookResponse)
def update_book(id:int,book:BookCreate,db:Session=Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id==id).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.genre = book.genre
    db_book.available_copies = book.available_copies
    db_book.total_copies=book.total_copies
    db.commit()
    db.refresh(db_book)
    return db_book  

@router.delete("/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):

    db_book = db.query(models.Book).filter(
        models.Book.id == id
    ).first()

    if not db_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    # Delete related borrow records first
    borrow_records = db.query(models.Borrow).filter(
        models.Borrow.book_id == id
    ).all()

    for record in borrow_records:
        db.delete(record)

    # Delete book
    db.delete(db_book)

    db.commit()

    return {"message": "Book deleted successfully"}
