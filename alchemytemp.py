
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Mapped, as_declarative, mapped_column, Session, declarative_base

from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class TestUser(Base):
    __tablename__ = 'testusers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


Base.metadata.create_all(engine)
testuser = TestUser(id=1, name='ffff')

with Session(engine) as session:
    
    session.add(testuser)
    session.commit()