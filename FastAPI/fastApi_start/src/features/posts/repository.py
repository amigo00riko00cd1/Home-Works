from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from .models import Post, Tag
from typing import List, Optional, Tuple

class PostRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _get_or_create_tags(self, tag_names: Optional[List[str]]) -> List[Tag]:
        if not tag_names:
            return []

        normalized = []
        for tag_name in tag_names:
            if not tag_name:
                continue
            clean_name = tag_name.strip().lower()
            if clean_name:
                normalized.append(clean_name)

        if not normalized:
            return []

        query = select(Tag).where(Tag.name.in_(normalized))
        result = await self.db.execute(query)
        existing_tags = {tag.name: tag for tag in result.scalars().all()}

        tags: List[Tag] = []
        for name in dict.fromkeys(normalized):
            if name in existing_tags:
                tags.append(existing_tags[name])
            else:
                new_tag = Tag(name=name)
                self.db.add(new_tag)
                tags.append(new_tag)

        return tags

    async def create_post(self, post_data: dict) -> Post:
        tags = post_data.pop("tags", [])
        new_post = Post(**post_data)
        if tags:
            new_post.tags = await self._get_or_create_tags(tags)
        self.db.add(new_post)
        await self.db.commit()
        await self.db.refresh(new_post)
        return new_post

    async def get_posts(self, skip: int = 0, limit: int = 10) -> Tuple[List[Post], int]:
        # Отримуємо загальну кількість
        total_query = select(func.count(Post.id))
        total_result = await self.db.execute(total_query)
        total = total_result.scalar() or 0

        # Отримуємо самі пости
        query = (
            select(Post)
            .options(selectinload(Post.author), selectinload(Post.likes), selectinload(Post.tags))
            .order_by(Post.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all(), total

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        from FastAPI.fastApi_start.src.features.comments.models import Comment

        query = (
            select(Post)
            .where(Post.id == post_id)
            .options(
                selectinload(Post.author),
                selectinload(Post.comments).selectinload(Comment.author),
                selectinload(Post.likes),
                selectinload(Post.tags)
            )
        )

        result = await self.db.execute(query)
        return result.scalar_one_or_none()
        
    async def get_user_posts(self, user_id: int, skip: int = 0, limit: int = 10) -> Tuple[List[Post], int]:
        from FastAPI.fastApi_start.src.features.comments.models import Comment

        total_query = select(func.count(Post.id)).where(Post.author_id == user_id)
        total_result = await self.db.execute(total_query)
        total = total_result.scalar() or 0

        query = (
            select(Post)
            .where(Post.author_id == user_id)
            .options(
                selectinload(Post.author),
                selectinload(Post.comments).selectinload(Comment.author),
                selectinload(Post.likes),
                selectinload(Post.tags)
            )
            .order_by(Post.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all(), total
