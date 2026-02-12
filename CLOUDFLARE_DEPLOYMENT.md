# ☁️ Cloudflare Deployment Guide

Deploy your silva-nanobot to Cloudflare for 24/7 availability.

## 🎯 Deployment Options

### Option 1: VPS + Cloudflare Tunnel (Recommended) ⭐

This is the easiest and most reliable method.

#### Step 1: Deploy to Any VPS

```bash
# On your VPS (DigitalOcean, AWS, etc.)
git clone https://github.com/YOUR_USERNAME/silva-nanobot.git
cd silva-nanobot
pip install -e .

# Configure
python -m nanobot onboard
# Edit ~/.nanobot/config.json with your API keys and Telegram token
```

#### Step 2: Install Cloudflare Tunnel

```bash
# Download cloudflared
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
sudo chmod +x /usr/local/bin/cloudflared

# Login to Cloudflare
cloudflared tunnel login
```

#### Step 3: Create Tunnel

```bash
# Create tunnel
cloudflared tunnel create silva-nanobot

# Get tunnel ID and credentials path (shown in output)
# Example: Tunnel credentials written to /root/.cloudflared/UUID.json
```

#### Step 4: Configure Tunnel

Create `~/.cloudflared/config.yml`:

```yaml
tunnel: YOUR_TUNNEL_ID
credentials-file: /root/.cloudflared/YOUR_TUNNEL_ID.json

ingress:
  # Main gateway endpoint
  - hostname: bot.yourdomain.com
    service: http://localhost:18790
  
  # Catch-all
  - service: http_status:404
```

#### Step 5: Start Everything

```bash
# Terminal 1: Start nanobot
python -m nanobot gateway

# Terminal  2: Start tunnel
cloudflared tunnel run silva-nanobot
```

#### Step 6: Use systemd (for auto-restart)

Create `/etc/systemd/system/nanobot.service`:

```ini
[Unit]
Description=Silva Nanobot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/silva-nanobot
ExecStart=/usr/local/bin/python -m nanobot gateway
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Create `/etc/systemd/system/cloudflared.service`:

```ini
[Unit]
Description=Cloudflare Tunnel
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/cloudflared tunnel run silva-nanobot
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable nanobot
sudo systemctl enable cloudflared
sudo systemctl start nanobot
sudo systemctl start cloudflared

# Check status
sudo systemctl status nanobot
sudo systemctl status cloudflared
```

---

### Option 2: Docker + Cloudflare Tunnel

#### Step 1: Build Docker Image

```bash
docker build -t silva-nanobot .
```

#### Step 2: Run Container

```bash
docker run -d --name silva-nanobot \
  -v ~/.nanobot:/root/.nanobot \
  -p 18790:18790 \
  --restart unless-stopped \
  silva-nanobot gateway
```

#### Step 3: Setup Cloudflare Tunnel

Follow the same tunnel setup as Option 1.

---

### Option 3: Cloudflare Workers (Telegram Webhook)

For Telegram-only deployment using serverless.

#### Step 1: Create Worker

```javascript
// worker.js
export default {
  async fetch(request, env) {
    if (request.method === "POST") {
      const update = await request.json();
      
      // Forward to your Kimi API or handle directly
      const response = await callKimiAPI(update.message.text, env);
      
      // Reply to Telegram
      await sendTelegramMessage(
        env.TELEGRAM_BOT_TOKEN,
        update.message.chat.id,
        response
      );
      
      return new Response("OK");
    }
    
    return new Response("Silva Nanobot is running!");
  }
};

async function callKimiAPI(message, env) {
  const response = await fetch("https://api.moonshot.ai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.MOONSHOT_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "moonshot-v1-128k",
      messages: [{ role: "user", content: message }],
      temperature: 1.0
    })
  });
  
  const data = await response.json();
  return data.choices[0].message.content;
}

async function sendTelegramMessage(token, chatId, text) {
  await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ chat_id: chatId, text })
  });
}
```

#### Step 2: Deploy Worker

```bash
# Install Wrangler
npm install -g wrangler

# Login
wrangler login

# Deploy
wrangler deploy
```

#### Step 3: Set Webhook

```bash
curl -X POST "https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://your-worker.workers.dev"}'
```

---

## 🔒 Environment Variables for Cloudflare

### For Workers

In Cloudflare Dashboard → Workers → Your Worker → Settings → Variables:

```
MOONSHOT_API_KEY=sk-your-key-here
TELEGRAM_BOT_TOKEN=your-telegram-token
```

### For VPS Deployment

Create `~/.nanobot/.env`:

```bash
MOONSHOT_API_KEY=sk-your-key-here
TELEGRAM_BOT_TOKEN=your-telegram-token
```

---

## 📊 Monitoring

### Check Logs

```bash
# Nanobot logs
sudo journalctl -u nanobot -f

# Cloudflare tunnel logs
sudo journalctl -u cloudflared -f

# Docker logs
docker logs -f silva-nanobot
```

### Health Check

```bash
# Check if nanobot is running
curl http://localhost:18790/health

# Check through Cloudflare tunnel
curl https://bot.yourdomain.com/health
```

---

## 💰 Cost Estimate

### Option 1: VPS + Cloudflare Tunnel
- **VPS**: $5-10/month (DigitalOcean, Linode)
- **Cloudflare Tunnel**: FREE
- **Total**: ~$5-10/month

### Option 2: Docker + Cloudflare Tunnel
- Same as Option 1

### Option 3: Cloudflare Workers
- **Workers**: FREE tier (100k requests/day)
- **Kimi API**: Pay per token
- **Total**: Mostly FREE for personal use

---

## 🚀 Recommended Setup

**For 24/7 Personal Use:**
- **Option 1** (VPS + Cloudflare Tunnel)
- Use a cheap $5/month VPS
- Zero configuration firewall needed
- Automatic HTTPS
- Full nanobot features

**For Serverless/Cost-Effective:**
- **Option 3** (Cloudflare Workers)
- Pay only for usage
- Automatic scaling
- Limited features (no local files, no system tools)

---

## 🆘 Troubleshooting

### Tunnel not connecting?
```bash
cloudflared tunnel list
cloudflared tunnel info silva-nanobot
```

### Worker not responding?
- Check Cloudflare Workers logs in dashboard
- Verify environment variables are set
- Test webhook: `curl -X POST https://your-worker.workers.dev`

### Bot not replying?
- Check nanobot is running: `python -m nanobot status`
- Verify Telegram webhook: `curl https://api.telegram.org/botYOUR_TOKEN/getWebhookInfo`
- Check logs for errors

---

**You're all set! Your assistant is now available 24/7** 🎉

