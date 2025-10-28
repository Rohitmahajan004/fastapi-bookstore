from pydantic import BaseModel
from typing import List, Optional

# -------- BOOK SCHEMAS --------
class BookBase(BaseModel):
    title: str
    genre: Optional[str] = None
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BaseModel):
    id: int
    title: str
    genre: Optional[str] = None
    author_id: int

    class Config:
        orm_mode = True


# -------- AUTHOR SCHEMAS --------
class AuthorBase(BaseModel):
    name: str
    country: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    books: List[BookResponse] = []

    class Config:
        orm_mode = True
