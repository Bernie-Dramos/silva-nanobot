# 🤖 Silva-Nanobot

**Your personal AI assistant powered by Kimi K2.5 (Moonshot AI)**

Based on [nanobot](https://github.com/HKUDS/nanobot) - the ultra-lightweight open-source AI assistant (~4,000 lines of code).

## ⚡ Quick Start

```bash
# Install
git clone https://github.com/YOUR_USERNAME/silva-nanobot.git
cd silva-nanobot
pip install -e .

# Configure
python -m nanobot onboard

# Set up Telegram (optional)
python setup_telegram.py

# Chat!
python -m nanobot agent -m "Hello!"

# Or start gateway for Telegram/Discord/etc.
python -m nanobot gateway
```

## ✨ Features

- 🧠 **Kimi K2.5** with 128K context window
- 💾 **Persistent Memory** - Remembers conversations across sessions
- 🛠️ **Full Tool Suite** - File operations, web search, bash commands
- 📱 **Multi-Channel** - Telegram, Discord, WhatsApp, Slack, Email, QQ, etc.
- ⏰ **Scheduling** - Cron jobs and automated tasks
- 🎯 **Skills System** - Loadable skill modules
- 🐳 **Docker Ready** - Production-ready containerization
- ☁️ **Cloud Deploy** - Easy deployment to any VPS with Cloudflare Tunnel

## 📱 Telegram Setup (2 minutes)

1. Create a bot with @BotFather on Telegram
2. Run `python setup_telegram.py` and follow prompts
3. Start gateway: `python -m nanobot gateway`
4. Chat with your bot!

## 📚 Documentation

- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Complete setup and usage guide
- **[CLOUDFLARE_DEPLOYMENT.md](./CLOUDFLARE_DEPLOYMENT.md)** - Production deployment  
- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Features and comparisons

## 🎯 Example Commands

```bash
# Interactive chat
python -m nanobot agent

# Single message
python -m nanobot agent -m "Create a Python web scraper"

# Schedule a task
python -m nanobot cron add --name "morning" --message "Good morning report" --cron "0 9 * * *"

# Check status
python -m nanobot status

# List tools
python -m nanobot agent -m "What tools do you have?"
```

## 🌟 Use Cases

- **Coding Assistant** - Create entire codebases, debug, refactor
- **Personal Assistant** - Reminders, scheduling, information lookup
- **Research Assistant** - Web search, summarization, knowledge management
- **System Admin** - Server monitoring, automation, log analysis

## 🔧 Configuration

Edit `~/.nanobot/config.json`:

```json
{
  "agents": {
    "defaults": {
      "model": "moonshot-v1-128k",
      "temperature": 1.0,
      "maxTokens": 8192
    }
  },
  "providers": {
    "moonshot": {
      "apiKey": "YOUR_API_KEY",
      "apiBase": "https://api.moonshot.ai/v1"
    }
  }
}
```

## ☁️ Cloud Deployment

Deploy to production in minutes:

```bash
# Option 1: VPS + Cloudflare Tunnel (recommended)
# See CLOUDFLARE_DEPLOYMENT.md for full guide

# Option 2: Docker
docker build -t silva-nanobot .
docker run -d -v ~/.nanobot:/root/.nanobot -p 18790:18790 silva-nanobot gateway

# Option 3: Cloudflare Workers
# See CLOUDFLARE_DEPLOYMENT.md for serverless deployment
```

## 💰 Costs

- **API**: Kimi K2.5 is very affordable (~$0.001-0.003 per 1K tokens)
- **Hosting**: $5-10/month VPS + FREE Cloudflare Tunnel
- **Total**: ~$5-15/month for 24/7 personal assistant

## 🔒 Security

For production:
- Set `restrictToWorkspace: true` in tools config
- Use `allowFrom` lists to restrict channel access
- Store API keys in environment variables
- Keep your config.json private

## 🛠️ Tech Stack

- **LLM**: Kimi K2.5 (moonshot-v1-128k) by Moonshot AI
- **Framework**: nanobot (Python)
- **Memory**: SQLite + semantic search
- **Channels**: Telegram, Discord, WhatsApp, Slack, Email, etc.
- **Deployment**: Docker, Systemd, Cloudflare Workers

## 📊 Architecture

```
┌─────────────────┐
│   Channels      │  Telegram, Discord, WhatsApp, CLI
│  (User Input)   │
└────────┬────────┘
         │
┌────────▼────────┐
│   Gateway/Bus   │  Message routing
└────────┬────────┘
         │
┌────────▼────────┐
│   Agent Loop    │  Tool calling, memory integration
└────────┬────────┘
         │
┌────────▼────────┐
│   Kimi K2.5     │  LLM inference (128K context)
└────────┬────────┘
         │
┌────────▼────────┐
│ Tools & Memory  │  File ops, web search, persistent memory
└─────────────────┘
```

## 🤝 Contributing

This is a personal fork of nanobot configured for Kimi K2.5. For core nanobot contributions, see the [upstream repository](https://github.com/HKUDS/nanobot).

## 📄 License

MIT License - Same as upstream nanobot

## 🙏 Acknowledgments

- [nanobot](https://github.com/HKUDS/nanobot) by HKUDS - The base framework
- [Moonshot AI](https://platform.moonshot.ai/) - Kimi K2.5 LLM provider
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM interface

---

**Ready to use your personal AI assistant!** 🚀

Get API key: https://platform.moonshot.ai/
Documentation: See SETUP_GUIDE.md

