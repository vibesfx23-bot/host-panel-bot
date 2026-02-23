# host-panel-bot
HOST BOT PANEL
📁 Project Structure

host-panel-bot/
├── .github/workflows/          # CI/CD pipelines
│   ├── ci.yml
│   └── deploy.yml
├── .env.example                # Env vars template
├── README.md                   # Full docs
├── requirements.txt            # Dependencies
├── docker-compose.yml          # Local dev/prod
├── Dockerfile
├── src/
│   ├── __init__.py
│   ├── main.py                 # Bot entrypoint
│   ├── config.py               # Config loader
│   ├── handlers/               # Telegram handlers
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── server.py
│   │   ├── hosting.py
│   │   └── utils.py
│   ├── api/                    # Hosting API clients
│   │   ├── __init__.py
│   │   ├── cpanel.py
│   │   ├── directadmin.py
│   │   └── whmcs.py
│   ├── database/               # DB models/migrations
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── migrations/
│   ├── middleware/             # Security/rate limiting
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── rate_limit.py
│   └── utils/                  # Helpers
│       ├── __init__.py
│       ├── logger.py
│       └── validators.py
├── tests/                      # Unit/integration tests
│   ├── test_handlers.py
│   ├── test_api.py
│   └── conftest.py
└── docs/                       # API docs
    └── api.md




# 🚀 Host Panel Bot

Telegram bot for managing hosting panels (cPanel, DirectAdmin, WHMCS).

## ✨ Features
- ✅ Server monitoring (CPU/RAM/Disk)
- ✅ Service restarts
- ✅ Backup management
- ✅ User/database management
- ✅ Real-time alerts

## 🛠️ Quick Start
```bash
cp .env.example .env
docker-compose up -d
python src/main.py
