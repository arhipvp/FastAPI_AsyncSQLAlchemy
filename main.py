import models
from models import database
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from models import models
from models.database import Base, engine
from routers.items import router as router_items

Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/create/")
def create_product(title:str,description:str,price:int,db: Session = Depends(get_db)):
    db_product = models.Category(id=1, name=title)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return  db_product

app.include_router(
    router=router_items
)
