from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import text


def create_book_with_audit(db: Session, book_in: schemas.BookCreate):
    """Create book and create an audit row in a single transaction."""
    try:
        new_book = models.Book(
            title=book_in.title,
            author=book_in.author,
            description=book_in.description,
            status=book_in.status
        )
        db.add(new_book)
        db.flush()  # get new_book.id

        audit = models.BookAudit(book_id=new_book.id, action="created")
        db.add(audit)
       
        db.commit()
        db.refresh(new_book)
        return new_book
    except Exception:
        db.rollback()
        raise


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()



def get_books(db: Session, skip: int = 0, limit: int = 10, status: str = None):
    q = db.query(models.Book)
    if status:
        q = q.filter(models.Book.status == status)
    return q.offset(skip).limit(limit).all()



def update_book(db: Session, book: models.Book, book_in: schemas.BookUpdate):
    for field, value in book_in.dict(exclude_unset=True).items():
        setattr(book, field, value)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book: models.Book):
    db.delete(book)
    db.commit()
    return True


def count_by_status(db: Session):
    stmt = text("SELECT status, COUNT(*) as cnt FROM books GROUP BY status")
    res = db.execute(stmt)
    return [{"status": row[0], "count": row[1]} for row in res]
