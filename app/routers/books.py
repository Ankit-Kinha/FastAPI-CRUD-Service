from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book_in: schemas.BookCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Book).filter(models.Book.title == book_in.title).first()
    if existing:
        raise HTTPException(status_code=400, detail="Book with this title already exists")
    return crud.create_book_with_audit(db, book_in)

@router.get("/", response_model=List[schemas.BookOut])
def list_books(skip: int = 0, limit: int = 10, status: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit, status=status)

@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book_in: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    # if new title conflicts
    if book_in.title and book_in.title != book.title:
        conflict = db.query(models.Book).filter(models.Book.title == book_in.title).first()
        if conflict:
            raise HTTPException(status_code=400, detail="Another book with this title exists")
    return crud.update_book(db, book, book_in)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book)
    return None

@router.get("/total_books/count", response_model=List[dict])
def counts(db: Session = Depends(get_db)):
    return crud.count_by_status(db)
