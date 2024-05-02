from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    address: str
    phone: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    quantity: int
    image: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    keyword: str

    class Config:
        orm_mode = True


class SearchHistoryBase(BaseModel):
    keyword: str
    user_id: int

class SearchHistoryCreate(SearchHistoryBase):
    pass
class SearchHistory(SearchHistoryBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True





class FavItemBase(BaseModel):
    user_id: int
    product_id: int

class FavItemCreate(FavItemBase):
    pass

class FavItem(FavItemBase):
    id: int

    class Config:
        orm_mode = True
