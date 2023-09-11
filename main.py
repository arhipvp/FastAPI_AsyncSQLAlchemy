from fastapi import FastAPI
from model import core
from model.database import engine, Base
from routers.items import router as router_items

Base.metadata.create_all(bind=engine)


app = FastAPI()

