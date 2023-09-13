import models
from models import database
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from models import models
from models.database import Base, engine
from routers.items import router as router_items

Base.metadata.create_all(bind=engine)


app = FastAPI()

