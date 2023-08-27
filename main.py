from fastapi import FastAPI
from routers.items import router as router_items

app = FastAPI()

app.include_router(
    router=router_items,
    prefix='/items',
)