from sqlalchemy.orm import Session
from db import models, schemas

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DbAauthor(name = author.name, second_name = author.second_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db:Session, author_id: int):
    return db.query(models.DbAauthor). filter(models.DbAauthor.id == author_id).first()

def get_authors(db:Session, skip:int=0, limit:int =50):
    return db.query(models.DbAauthor).offset(skip).limit(limit).all()



def create_book(db: Session, book: schemas.BookCreate, author: int, content, img):

    path = f'static/images/{img.filename}'
    with open(path, 'wb') as image:
        image.write(content)

    db_book = models.DbBook(title = book.title, pages = book.pages, author = author, img_path = path)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book



def get_book(db: Session, book_id: int):
    return db.query(models.DbBook).filter(models.DbBook.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.DbBook).offset(skip).limit(limit).all()

