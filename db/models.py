from sqlalchemy import Column, Integer, String, ForeignKey
from .engine import Base
from sqlalchemy.orm import relationship

class DbAauthor(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key = True, index = True )
    name = Column(String(63), nullable = False)
    second_name = Column(String(62), nullable = False)



class DbBook(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(63), nullable = False)
    pages = Column(Integer, nullable = False)
    author = Column(String(63), nullable = False)
    info = Column(String(63), nullable = False)
    img_path = Column(String, nullable='False')



class BbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index = True)
    login = Column(String(40), nullable = False, unique = True)
    password = Column(String(40), nullable = False, unique = True)

