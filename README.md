# Multi-Platform-Content-Publisher

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

> **Showcase** — ~15% skeleton. Core implementation not included.

Automated daily publishing pipeline. Fetches trending topics, generates platform-specific copy via Claude, publishes to 9 platforms, and auto-replies to comments. A Lark bot reports results in real time.

## Stack

- Python
- Claude Code CLI
- Playwright (browser automation)
- Lark (Feishu) Bot API

## Platforms

Juejin, Zhihu, CSDN, Sohu, Toutiao, Cnblogs, Sspai, Twitter, WeChat (read-only notify)

## Pipeline

```
Trending topic fetch
    └── Claude CLI: generate per-platform copy
         └── Playwright / HTTP API: publish
              └── Lark bot: send result card
                   └── Comment monitor: auto-reply
```

The scheduler runs once per day. Each platform adapter handles login state via saved Playwright storage.

## Usage

```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml   # fill in API keys and account credentials

# Dry run (generate copy, skip publish)
python run.py --dry-run

# Full run
python run.py

# Publish to a single platform
python run.py --platform juejin
```

## Structure

```
Multi-Platform-Content-Publisher/
├── adapters/          # one file per platform
│   ├── juejin.py
│   ├── zhihu.py
│   └── ...
├── generator/         # Claude CLI wrapper and prompt templates
├── notifier/          # Lark bot integration
├── scheduler/         # cron entry point
├── run.py
└── config.example.yaml
```

## Configuration

`config.yaml` fields:

| Key | Description |
|-----|-------------|
| `claude.model` | Claude model to use |
| `platforms.<name>.enabled` | toggle per platform |
| `lark.webhook` | Lark bot webhook URL |
| `schedule.cron` | cron expression for daily run |
