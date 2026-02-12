# 🐈 Silva-Nanobot - Personal AI Assistant powered by Kimi K2.5

Your personal AI assistant based on nanobot with Kimi K2.5 (Moonshot AI) backend.

## ✅ Current Status

- ✅ **Nanobot installed and configured**
- ✅ **Kimi K2.5 (moonshot-v1-128k) set as default model**
- ✅ **128K context window available**
- ✅ **Persistent memory system active**
- ✅ **Full tool suite enabled**
- ✅ **CLI working**
- ⏳ **Telegram integration (setup below)**

## 🚀 Quick Start

### Test Locally

```bash
# Chat via CLI
python -m nanobot agent -m "What can you do?"

# Interactive mode
python -m nanobot agent

# Check status
python -m nanobot status
```

## 📱 Telegram Setup

### 1. Create Your Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow the prompts to name your bot
4. Copy the **bot token** you receive

### 2. Get Your User ID

1. Search for `@userinfobot` in Telegram
2. Start a chat with it
3. It will show your **User ID** (a number like `123456789`)

### 3. Configure Telegram

Edit `~/.nanobot/config.json` (or `C:\Users\bdram\.nanobot\config.json`):

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN_HERE",
      "allowFrom": ["YOUR_USER_ID_HERE"],
      "proxy": null
    }
  }
}
```

### 4. Start the Gateway

```bash
python -m nanobot gateway
```

Now chat with your bot on Telegram! 🎉

## 🛠️ Features

### Core Tools

- **Shell/Bash**: Execute commands
- **File Operations**: Read, write, edit files
- **Web Search**: Search the internet
- **Process Management**: Run and manage processes
- **Memory**: Persistent conversation memory
- **Skills**: Loadable skill modules

### Persistent Memory

- Automatically remembers conversations
- Semantic search across history
- Context-aware responses
- Long-term learning

### Cron/Scheduling

```bash
# Schedule a task
python -m nanobot cron add --name "morning" --message "Good morning report" --cron "0 9 * * *"

# List scheduled tasks
python -m nanobot cron list

# Remove a task
python -m nanobot cron remove <job_id>
```

### Workspace Management

- Files created by the assistant are stored in `~/.nanobot/workspace/`
- Code generation and project creation
- Safe sandboxed environment

## 🐳 Docker Deployment (for Cloudflare or Production)

### Build Image

```bash
docker build -t silva-nanobot .
```

### Run with Docker

```bash
# Initialize (first time)
docker run -v ~/.nanobot:/root/.nanobot --rm silva-nanobot onboard

# Edit config to add your API keys and Telegram token
# Then run gateway
docker run -d --name silva-nanobot \
  -v ~/.nanobot:/root/.nanobot \
  -p 18790:18790 \
  --restart unless-stopped \
  silva-nanobot gateway
```

## ☁️ Cloudflare Deployment

### Option 1: Cloudflare Workers (for API/Webhook)

Create a webhook handler for Telegram bot updates.

### Option 2: Cloudflare Pages (with Functions)

Deploy the Docker container on Cloudflare's infrastructure.

### Option 3: VPS with Cloudflare Tunnel

1. Deploy Docker container on any VPS
2. Use Cloudflare Tunnel for secure access
3. No public ports needed

```bash
# Install cloudflared
# Create tunnel
cloudflared tunnel create silva-nanobot

# Configure tunnel
# In your config.yml:
ingress:
  - hostname: silva-nanobot.yourdomain.com
    service: http://localhost:18790
  - service: http_status:404

# Run tunnel
cloudflared tunnel run silva-nanobot
```

## 📊 Configuration Details

### Current Model: Kimi K2.5 (moonshot-v1-128k)
- **Context**: 128,000 tokens
- **Temperature**: 1.0 (recommended by Moonshot)
- **Max Tokens**: 8,192
- **API Base**: https://api.moonshot.ai/v1

### Tools Configuration
- **Restrict to Workspace**: `false` (set to `true` for production)
- **Exec Timeout**: 60 seconds
- **Web Search**: Configurable (add Brave API key for better results)

## 🔐 Security

For production deployment:

1. **Enable workspace restriction**:
```json
{
  "tools": {
    "restrictToWorkspace": true
  }
}
```

2. **Set allowFrom lists**:
```json
{
  "channels": {
    "telegram": {
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

3. **Use environment variables** for sensitive data

## 📁 File Structure

```
~/.nanobot/
├── config.json          # Main configuration
├── workspace/           # Agent workspace (code, files)
├── memory/              # Persistent memory database
└── sessions/            # Session data
```

## 🌟 Example Use Cases

### As a Coding Assistant

```
You: Create a Python web scraper for news headlines
Bot: [Creates files in workspace, explains code, ready to run]
```

### As a Personal Assistant

```
You: Remind me to check emails every morning at 9 AM
Bot: [Sets up cron job, confirms scheduling]
```

### As a Research Assistant

```
You: Research the latest developments in AI agents and summarize
Bot: [Searches web, synthesizes information, stores findings]
```

## 🔧 Troubleshooting

### Bot not responding on Telegram?
- Check gateway is running: `python -m nanobot status`
- Verify token in config.json
- Check your User ID is in allowFrom list

### Model errors?
- Verify API key is correct
- Check API base URL: `https://api.moonshot.ai/v1`
- Ensure temperature is >= 1.0 for Kimi K2.5

### Memory not working?
- Memory is automatic, check `~/.nanobot/memory/`
- Try asking: "What did we talk about yesterday?"

## 📚 Resources

- [Nanobot Documentation](https://github.com/HKUDS/nanobot)
- [Moonshot AI Platform](https://platform.moonshot.ai/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 🚀 Next Steps

1. ✅ Set up Telegram bot
2. Test all features via Telegram
3. Deploy to production (Docker + Cloudflare)
4. Add more skills from the skills/ directory
5. Customize prompts and behavior
6. Enable web search with Brave API

---

**Enjoy your personal AI assistant!** 🎉

