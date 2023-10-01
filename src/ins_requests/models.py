from datetime import datetime

from sqlalchemy import (TIMESTAMP, Column, DateTime, Integer, MetaData, String,
                        Table)
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class InsRequest(Base):
    __tablename__ = "ins_request"
    __metadata__ = Base.metadata
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String)
    note = mapped_column(String)
    state = mapped_column(Integer)
    created_at = mapped_column(DateTime, default=datetime.utcnow)


# ins_request = Table(
#     'ins_request',
#     metadata,
#     Column('id', Integer, autoincrement=True, primary_key=True),
#     Column('name', String),
#     Column('note', String),
#     Column('state', Integer),
#     Column('created_at', TIMESTAMP),
#     )
