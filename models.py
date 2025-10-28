from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete")

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)

    author = relationship("Author", back_populates="book")
