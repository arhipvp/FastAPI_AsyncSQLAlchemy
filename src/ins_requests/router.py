from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.ins_requests.models import InsRequest
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/req',
    tags=['req'],
)

@router.get('/id')
async def get_ins_req(id: int, session: AsyncSession = Depends(get_async_session)):
    sql = select(InsRequest).where(InsRequest.id == id)
    result = await session.execute(sql)
    return result.scalar_one_or_none()

@router.get('/all')
async def get_ins_req(session: AsyncSession = Depends(get_async_session)):
    sql = select(InsRequest)
    result = await session.execute(sql)
    return result.scalars().all()

@router.post('')
async def post_ins_req(name: str, note: str, session: AsyncSession = Depends(get_async_session)):
    new_ins_request = InsRequest(name=name, note=note)
    session.add(new_ins_request)
    await session.commit()
    return new_ins_request

@router.patch('')
async def patch_ins_req(id: int, name: str, note: str, session: AsyncSession = Depends(get_async_session)):
    patch_ins_req = await session.get(InsRequest, id)
    patch_ins_req.name = name
    patch_ins_req.note = note
    #await session.refresh(patch_ins_req, name =name, note=note)
    #await session.refresh(patch_ins_req)
    await session.commit()
    return patch_ins_req



@router.delete('')
async def delete_ins_request(id: int, session: Session = Depends(get_async_session)):
    ins_request = await session.get(InsRequest, id)
    print(ins_request)
    
    await session.delete(ins_request)
    await session.commit()
    
    return ins_request