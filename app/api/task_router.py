from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.db_init import get_db_session
from ..repositories.repositories import UserRepository
from ..schemas import TaskCreate, Task


router = APIRouter()


@router.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.create_task(task.dict())


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.get_task(task_id)


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.update_task(task_id, task.dict())


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    await user_repo.delete_task(task_id)
    return {"message": "Task deleted"}

