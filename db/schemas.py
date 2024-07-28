from pydantic import BaseModel

class AuthorBase(BaseModel):
    name:str
    second_name:str


class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Cofig:
        from_attributes = True

######################################

class BookBase(BaseModel):
    title: str
    pages: int
    author: str
    info: str
    img_path: str



class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: str
    img_path: str

    class Cofig:
        from_attributes = True

#################################

class UserBase(BaseModel):
    login: int
    password: str



class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Cofig:
        from_attributes = True