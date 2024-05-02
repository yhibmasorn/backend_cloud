from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"ทำได้": "แร้ววววว"}


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes for User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    state = crud.get_user_all(db, skip=skip, limit=limit)
    return state

@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Routes for Product
@app.post("/product/", response_model=schemas.Product)
def create_product(keyword: str , product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_tick = crud.get_search_keyword(db, keyword)

    if not db_tick:
        raise HTTPException(status_code=400, detail="keyword not found")

    return crud.create_product(db=db, product=product, 
                               keyword=keyword)


@app.get("/product/", response_model=list[schemas.Product])
def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    state = crud.get_product_all(db, skip=skip, limit=limit)
    return state

@app.get("/product/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Routes for FavItem
@app.post("/fav/", response_model=schemas.FavItem)
def create_fav_item(fav_item: schemas.FavItemCreate, db: Session = Depends(get_db)):
    return crud.create_fav_item(db=db, fav_item=fav_item)

@app.get("/fav/{fav_item_id}", response_model=schemas.FavItem)
def read_fav_item(fav_item_id: int, db: Session = Depends(get_db)):
    db_fav_item = crud.get_fav_item(db=db, fav_item_id=fav_item_id)
    if db_fav_item is None:
        raise HTTPException(status_code=404, detail="Fav item not found")
    return db_fav_item

# Routes for SearchHistory
@app.post("/search/", response_model=schemas.SearchHistory)
def create_search_history(search_history: schemas.SearchHistoryCreate, db: Session = Depends(get_db)):
    return crud.create_search_history(db=db, search_history=search_history)

@app.get("/search/", response_model=list[schemas.SearchHistory])
def read_search(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    state = crud.get_search_all(db, skip=skip, limit=limit)
    return state

@app.get("/search/{user_id}", response_model=schemas.SearchHistory)
def read_search_history(user_id: int, db: Session = Depends(get_db)):
    db_search_history = crud.get_search_history(db=db, user_id=user_id)
    if db_search_history is None:
        raise HTTPException(status_code=404, detail="Search history not found")
    return db_search_history