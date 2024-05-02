# crud.py
from sqlalchemy.orm import Session

from . import models, schemas



# SearchHistory CRUD operations
def create_search_history(db: Session, search_history: schemas.SearchHistoryCreate):
    db_search_history = models.SearchHistory(keyword=search_history.keyword,
                                             user_id=search_history.user_id)
    db.add(db_search_history)
    db.commit()
    db.refresh(db_search_history)
    return db_search_history

def get_search_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SearchHistory).offset(skip).limit(limit).all()

def get_search_history(db: Session, user_id: int):
    return db.query(models.SearchHistory).filter(models.SearchHistory.id == user_id).first()

def get_search_keyword(db: Session, keyword: str):
    return db.query(models.SearchHistory).filter(models.SearchHistory.keyword == keyword).first()

# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Product CRUD operations


def create_product(db: Session, product: schemas.ProductCreate, keyword: str):
    search_history = db.query(models.SearchHistory).filter(models.SearchHistory.keyword == keyword).first()
    if not search_history:
        return None  # No search history found with the given keyword

    # Create the product and associate it with the found search history
    db_product = models.Product(name=product.name,
                                description=product.description,
                                price=product.price,
                                quantity=product.quantity,
                                image=product.image,
                                keyword=keyword)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# FavItem CRUD operations
def create_fav_item(db: Session, fav_item: schemas.FavItemCreate):
    db_fav_item = models.FavItem(**fav_item.dict())
    db.add(db_fav_item)
    db.commit()
    db.refresh(db_fav_item)
    return db_fav_item

def get_fav_item(db: Session, fav_item_id: int):
    return db.query(models.FavItem).filter(models.FavItem.id == fav_item_id).first()
