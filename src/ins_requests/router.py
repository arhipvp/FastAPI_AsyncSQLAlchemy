from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.ins_requests.models import InsRequest
from src.ins_requests.schemas import GetInsRequest

router = APIRouter(
    prefix='/req',
    tags=['req'],
)

@router.get("")
async def get_ins_req(
        operation_type: int,
        session: AsyncSession = Depends(get_async_session),
):
    new = InsRequest(name = 'ggg')
    with session.begin
        session.add(new)
        return result