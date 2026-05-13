<div align="center">

# ✍️ Multi-Platform Content Publisher

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Claude](https://img.shields.io/badge/Claude-CLI-D4A843?style=flat-square&logo=anthropic&logoColor=white)](https://claude.ai)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33?style=flat-square&logo=playwright&logoColor=white)](https://playwright.dev)
[![Lark](https://img.shields.io/badge/Lark-Bot-00D6B9?style=flat-square&logo=bytedance&logoColor=white)](https://open.feishu.cn)

**End-to-end AI content automation: hotspot harvesting → daily article generation → 9-platform publishing → comment reply, no human-in-the-loop**

> ⚠️ **Showcase Only** — ~15% skeleton. Platform credentials, anti-bot logic & production schedulers not included.

</div>

---

## ✨ Overview

A fully autonomous content pipeline that publishes AI-tech articles to **9 platforms every day** — sourcing fresh hotspots, generating platform-specific copy with Claude CLI, then publishing via either browser automation (Playwright) or direct HTTP APIs. A Lark bot ("Murphy") notifies the team for every publish and reply.

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────┐
│   Daily Schedule (cron)                                │
└─────────┬──────────────────────────────────────────────┘
          │ 09:00
          ▼
 ┌────────────────────┐       ┌───────────────────────┐
 │  Intel Harvester   │──────►│  data/intel/*.json    │
 │  HN · GH Trending  │       │   (cached hotspots)    │
 │  V2EX              │       └───────────┬───────────┘
 └────────────────────┘                   │
                                          │
                                          ▼
                              ┌───────────────────────┐
                              │  Claude CLI Writer    │
                              │  (per-platform style) │
                              └───────────┬───────────┘
                                          │
            ┌──────────────────┬──────────┴──────────┬──────────────┐
            ▼                  ▼                     ▼              ▼
       Juejin            Zhihu             CSDN / 头条 / ...    Twitter
      (Playwright)     (Playwright)            (Playwright)       (API)
            │                  │                     │              │
            └──────────────────┴─────────┬───────────┴──────────────┘
                                         │
                                         ▼
                              ┌───────────────────────┐
                              │  Lark Bot · Murphy    │
                              │  green card + link    │
                              └───────────────────────┘
```

---

## 🌍 Supported Platforms

| Platform | Method | Daily Slot |
|---|---|---|
| 掘金 Juejin | Playwright | 10:00 |
| 知乎 Zhihu | Playwright | 11:00 |
| CSDN | Playwright | 12:00 |
| 搜狐 Sohu | Playwright | 13:00 |
| 头条 Toutiao | Playwright | 14:00 |
| 博客园 Cnblogs | Playwright | 15:00 |
| 少数派 Sspai | Playwright | 16:00 |
| Twitter | HTTP API | rolling |
| Intel digest | Lark | 09:00 |

---

## 📁 Structure

```
multi-platform-content-publisher/
├── src/
│   ├── publishers/
│   │   ├── base.py            # BasePublisher interface
│   │   └── zhihu.py           # Zhihu publisher (example)
│   ├── intel/
│   │   └── hotspot_fetcher.py # HN / GH Trending fetcher
│   └── lark/
│       └── murphy_bot.py      # Murphy notification bot
├── prompts/                    # Per-platform style prompts
└── requirements.txt
```

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Content Generation | Claude CLI (no API key needed) |
| Browser Automation | Playwright (Chromium) |
| Hotspot Sources | Hacker News · GitHub Trending · V2EX |
| Notification | Lark / Feishu Bot |
| Scheduler | systemd timer / cron |

---

<div align="center">
<sub>Showcase version · Anti-bot & credential logic not included · For portfolio reference only</sub>
</div>
