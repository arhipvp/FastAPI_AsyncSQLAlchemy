
from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative

from src.database import Base, engine, get_async_session

session = get_async_session()

print(session)
print(Base.metadata.info)


@as_declarative(metadata=Base.metadata)
class TestUser:
    __tablename__ = 'testusers'
    id = Column(Integer, primary_key=True)
    
