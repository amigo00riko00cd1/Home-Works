from sqlalchemy import String, ForeignKey, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from FastAPI.fastApi_start.src.infrastructure.base_model import Base, TimestampMixin
from typing import List, Optional

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)

class Post(Base, TimestampMixin):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)

    # Відносини
    author: Mapped["User"] = relationship("User", backref="posts")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    likes: Mapped[List["Like"]] = relationship("Like", back_populates="post", cascade="all, delete-orphan")
    tags: Mapped[List["Tag"]] = relationship(
        "Tag",
        secondary=post_tags,
        back_populates="posts",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"Post(id={self.id}, author_id={self.author_id})"

class Tag(Base, TimestampMixin):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)

    posts: Mapped[List["Post"]] = relationship(
        "Post",
        secondary=post_tags,
        back_populates="tags",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, name={self.name})"

# Для коректної роботи relationship нам потрібно імпортувати інші моделі
# Використовуємо TYPE_CHECKING або імпортуємо в кінці файлу для SQLAlchemy
from FastAPI.fastApi_start.src.features.auth.models import User
from FastAPI.fastApi_start.src.features.comments.models import Comment
from FastAPI.fastApi_start.src.features.likes.models import Like
