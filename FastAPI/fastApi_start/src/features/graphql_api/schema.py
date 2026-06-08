import strawberry
from typing import List, Optional
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from FastAPI.fastApi_start.src.features.posts.models import Post
from FastAPI.fastApi_start.src.features.comments.models import Comment
from sqlalchemy.ext.asyncio import AsyncSession

@strawberry.type
class UserType:
    id: int
    email: str

@strawberry.type
class CommentType:
    id: int
    content: str
    author: UserType
    created_at: datetime

@strawberry.type
class PostType:
    id: int
    content: str
    image_url: Optional[str]
    created_at: datetime
    author: UserType
    likes_count: int
    tags: List[str]
    comments: List[CommentType]

@strawberry.type
class Query:
    @strawberry.field
    async def all_posts(self, info: strawberry.Info, limit: int = 10, offset: int = 0) -> List[PostType]:
        """
        Отримати список постів з усіма вкладеними даними.
        Демонструє силу GraphQL: фронтенд сам вирішує, які поля йому потрібні.
        """
        db: AsyncSession = info.context["db"]
        
        # Формуємо запит з жадібним завантаженням всіх необхідних зв'язків
        query = (
            select(Post)
            .options(
                selectinload(Post.author), 
                selectinload(Post.likes),
                selectinload(Post.comments).selectinload(Comment.author),
                selectinload(Post.tags)
            )
            .order_by(Post.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        
        result = await db.execute(query)
        posts = result.scalars().all()
        
        return [
            PostType(
                id=p.id,
                content=p.content,
                image_url=p.image_url,
                created_at=p.created_at,
                author=UserType(id=p.author.id, email=p.author.email),
                likes_count=len(p.likes),
                tags=[tag.name for tag in p.tags] if p.tags else [],
                comments=[
                    CommentType(
                        id=c.id,
                        content=c.content,
                        created_at=c.created_at,
                        author=UserType(id=c.author.id, email=c.author.email)
                    ) for c in p.comments
                ]
            ) for p in posts
        ]

schema = strawberry.Schema(query=Query)
