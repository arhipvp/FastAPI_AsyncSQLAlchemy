from sqlalchemy import (JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        MetaData, String, Table, Time)
from sqlalchemy.orm import declarative_base, relationship

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON),
)

users = Table(
    'users',
    metadata,
    Column('id', primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('regastared_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey=('roles.id')),
)




# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

#     #items = relationship('Furniture', back_populates='category_id')

# class Furniture(Base):
#     __tablename__ = 'furniture'
    
#     id = Column(Integer, primary_key=True, index=True)
#     #category_id = Column(Integer, ForeignKey('category.id'))
#     name = Column(String)
#     width = Column (Integer)
#     height = Column (Integer)
#     created_at = Column(Time)
