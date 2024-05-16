import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from app.models import User, Booster, Task
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_data: dict) -> User:
        new_user = User(**user_data)
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def read_user(self, user_id: int) -> User:
        async with self.session.begin():
            query = select(User).filter_by(id=user_id)
            result = await self.session.execute(query)
            try:
                user = result.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="User not found")
            return user

    async def update_user(self, user_id: int, update_data: dict):
        async with self.session.begin():
            query = select(User).where(User.id == user_id)
            result = await self.session.execute(query)
            user = result.scalars().first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            for key, value in update_data.items():
                setattr(user, key, value)
            await self.session.commit()
            return user

    async def delete_user(self, user_id: int) -> None:
        async with self.session.begin():
            query = select(User).filter_by(id=user_id)
            result = await self.session.execute(query)
            try:
                user = result.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="User not found")
            await self.session.delete(user)
            await self.session.commit()

    async def create_booster(self, booster_data: dict) -> Booster:
        new_booster = Booster(**booster_data)
        self.session.add(new_booster)
        await self.session.commit()
        await self.session.refresh(new_booster)
        return new_booster

    async def get_booster(self, booster_id: int) -> Booster:
        async with self.session.begin():
            query = select(Booster).filter_by(id=booster_id)
            result = await self.session.execute(query)
            try:
                booster = result.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Booster not found")
            return booster

    async def update_booster(self, booster_id: int, booster_data: dict) -> Booster:
        async with self.session.begin():
            query = select(Booster).filter_by(id=booster_id)
            result = await self.session.execute(query)
            booster = result.scalars().first()
            if not booster:
                raise HTTPException(status_code=404, detail="Booster not found")
            for key, value in booster_data.items():
                setattr(booster, key, value)
            await self.session.refresh(booster)
            return booster


    async def create_task(self, task_data: dict) -> Task:
        new_task = Task(**task_data)
        self.session.add(new_task)
        await self.session.commit()
        await self.session.refresh(new_task)
        return new_task

    async def get_task(self, task_id: int) -> Task:
        async with self.session.begin():
            query = select(Task).filter_by(id=task_id)
            result = await self.session.execute(query)
            try:
                task = result.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Task not found")
            return task

    async def update_task(self, task_id: int, task_data: dict) -> Task:
        async with self.session.begin():
            query = select(Task).filter_by(id=task_id)
            result = await self.session.execute(query)
            task = result.scalars().first()
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            for key, value in task_data.items():
                setattr(task, key, value)
            await self.session.refresh(task)
            return task

    async def delete_task(self, task_id: int) -> None:
        async with self.session.begin():
            query = select(Task).filter_by(id=task_id)
            result = await self.session.execute(query)
            try:
                task = result.scalar_one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Task not found")
            await self.session.delete(task)
            await self.session.commit()