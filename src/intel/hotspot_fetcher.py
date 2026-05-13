"""
Hotspot fetcher: aggregates daily tech news from multiple sources.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Hotspot:
    source: str
    title: str
    url: str
    score: int
    summary: str = ""


class HotspotFetcher:
    SOURCES = ["hackernews", "github_trending", "v2ex"]

    async def fetch_all(self) -> List[Hotspot]:
        """Fetch & dedupe hotspots from all sources. [Not shown]"""
        pass

    async def _fetch_hn(self) -> List[Hotspot]:
        """Hacker News top stories. [Not shown]"""
        pass

    async def _fetch_github_trending(self) -> List[Hotspot]:
        """GitHub trending repos (daily). [Not shown]"""
        pass
