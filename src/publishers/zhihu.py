"""
Zhihu publisher — Playwright automation against editor.zhihu.com.
"""

from .base import BasePublisher, Article, PublishResult


class ZhihuPublisher(BasePublisher):
    PLATFORM = "zhihu"

    def __init__(self, cookie_path: str, headless: bool = True):
        self.cookie_path = cookie_path
        self.headless = headless
        # [Browser context init not shown]

    async def login(self) -> None:
        """Load saved cookies into Playwright context. [Not shown]"""
        pass

    async def publish(self, article: Article) -> PublishResult:
        """Open editor, fill title + body, click publish. [Not shown]"""
        pass

    async def fetch_comments(self, post_url: str) -> list:
        """Parse comment list on the article page. [Not shown]"""
        pass
