"""
Murphy — Lark bot for publish notifications and daily digests.
"""

from typing import Optional


class MurphyBot:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    async def notify_publish(self, platform: str, title: str, url: str,
                              word_count: int, cover: Optional[str] = None):
        """Send green-card publish notification. [Not shown]"""
        pass

    async def notify_reply(self, platform: str, comment: str, reply: str):
        """Send comment-reply notification. [Not shown]"""
        pass
