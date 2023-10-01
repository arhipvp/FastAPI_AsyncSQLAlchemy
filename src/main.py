import fastapi_users
from fastapi import Depends, FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead
from src.ins_requests.router import router as ins_requests_router

from .database import Base, engine

app = FastAPI()





app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


#======================================================#

app.include_router(
    ins_requests_router,
)