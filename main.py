from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.engine import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing_extensions import Annotated
from db import models, schemas, crud
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

models.Base.metadata.create_all(bind = engine)

app = FastAPI()
print('first')

template = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="index")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/static", StaticFiles(directory="static"), name="static")


user_name = 'admin'
password = '1'


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/book")
def booklist(request:Request, skip: int=0 , limit: int=50, db:Session= Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return template.TemplateResponse("first.html", {'request': request, 'books': books})

@app.get("/book_list")
def booklists(request:Request, skip: int=0 , limit: int=50, db:Session= Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    #books = [models.DbBook.title, models.DbBook.author]
    
    return template.TemplateResponse("book_list.html", {'request': request, 'books': books})




@app.post("/token")
async def token_get(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if form_data.username != user_name or form_data.password != password:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")

    return {"access_token": form_data.username, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    return {"message": "Ці дані доступні лише авторизованим користувачам"}


@app.post('/author/add/', response_model=schemas.Author)
def add_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get('author/get/', response_model=schemas.Author)
def get_author(author: str, db: Session = Depends(get_db)):
    return crud.get_author(db, author)

@app.post('/{author_id}/add/', response_model=schemas.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user: str=Depends(protected)):
    return crud.create_book(db=db, book=book)

@app.get('book/get/', response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db, book_id)