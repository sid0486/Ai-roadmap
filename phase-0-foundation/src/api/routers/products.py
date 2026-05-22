from fastapi import APIRouter , HTTPException ,Depends 
from sqlalchemy.orm import Session
from src.db import models 
from src.db.database import get_db
from src.schema.products import ProductCreate,ProductResponse

router = APIRouter()


@router.get("/", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    seed(db)
    return db.query(database_models.Product).all()


@router.get("/{id}", response_model=Product)
def get_product(id: int, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    return row


@router.post("/", response_model=Product, status_code=201)
def add_product(product:ProductCreate, db: Session = Depends(get_db)):
    row = database_models.Product(**product.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.put("/{id}", response_model=Product)
def update_product(id: int, product:ProductCreate, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    for k, v in product.model_dump().items():
        setattr(row, k, v)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(row)
    db.commit()
    return {"message": "Product deleted"}