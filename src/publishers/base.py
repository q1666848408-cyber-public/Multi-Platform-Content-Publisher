"""
Base publisher interface. All platform publishers inherit from this.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Article:
    title: str
    body_markdown: str
    tags: list
    cover_image: Optional[str] = None


@dataclass
class PublishResult:
    success: bool
    url: Optional[str] = None
    error: Optional[str] = None


class BasePublisher(ABC):
    PLATFORM: str = ""

    @abstractmethod
    async def login(self) -> None:
        """Authenticate / load cookies. [Not shown]"""
        pass

    @abstractmethod
    async def publish(self, article: Article) -> PublishResult:
        """Publish an article. [Not shown]"""
        pass

    @abstractmethod
    async def fetch_comments(self, post_url: str) -> list:
        """Fetch new comments for reply automation. [Not shown]"""
        pass
