from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class URL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str = Field(index=True, unique=True, max_length=10)
    target_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    clicks: int = Field(default=0)
