#!/usr/bin/env python3
"""
Quick Telegram Setup Script for Silva-Nanobot
Helps you configure Telegram integration quickly
"""
import json
import os
from pathlib import Path


def main():
    print("🤖 Silva-Nanobot - Telegram Setup")
    print("=" * 50)
    print()
    
    # Find config file
    config_path = Path.home() / ".nanobot" / "config.json"
    
    if not config_path.exists():
        print("❌ Config file not found. Please run 'python -m nanobot onboard' first.")
        return
    
    # Load config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print("📱 Step 1: Create a Telegram Bot")
    print("-" * 50)
    print("1. Open Telegram and search for @BotFather")
    print("2. Send /newbot and follow the prompts")
    print("3. Copy the bot token you receive")
    print()
    
    bot_token = input("Enter your bot token: ").strip()
    
    if not bot_token:
        print("❌ No token provided. Exiting.")
        return
    
    print()
    print("👤 Step 2: Get Your User ID")
    print("-" * 50)
    print("1. Open Telegram and search for @userinfobot")
    print("2. Start a chat with it")
    print("3. Copy your User ID (a number like 123456789)")
    print()
    
    user_id = input("Enter your User ID: ").strip()
    
    if not user_id:
        print("❌ No user ID provided. Exiting.")
        return
    
    # Update config
    config['channels']['telegram']['enabled'] = True
    config['channels']['telegram']['token'] = bot_token
    config['channels']['telegram']['allowFrom'] = [user_id]
    
    # Save config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print()
    print("=" * 50)
    print("✅ Telegram configured successfully!")
    print("=" * 50)
    print()
    print("🚀 Next Steps:")
    print("1. Start the gateway:")
    print("   python -m nanobot gateway")
    print()
    print("2. Open Telegram and send a message to your bot")
    print()
    print("3. Enjoy your personal AI assistant! 🎉")
    print()
    print("📝 Config saved to:", config_path)


if __name__ == "__main__":
    main()
