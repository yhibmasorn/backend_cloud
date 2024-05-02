from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class SearchHistory(Base):
    __tablename__ = 'searchs'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    keyword = Column(String)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), index=True)  
 
    usersearch = relationship("User", back_populates="searching")
    searchproduct = relationship("Product", back_populates="productsearch")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    address = Column(String)
    phone = Column(Integer)

    searching = relationship("SearchHistory", back_populates="usersearch")
    userfav = relationship("FavItem", back_populates="favuser")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    image = Column(String)
    keyword = Column(String, ForeignKey('searchs.keyword'))

    productsearch = relationship("SearchHistory", back_populates="searchproduct")
    productfav = relationship("FavItem", back_populates="favproduct")

class FavItem(Base):
    __tablename__ = 'fav'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
   
    favuser = relationship("User", back_populates="userfav")
    favproduct = relationship("Product", back_populates="productfav")

