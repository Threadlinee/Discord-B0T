## TL;DR:

## For your reminder bot that just sends messages, either enable the intent in portal (recommended if you plan to read messages later) or turn off message_content in code if you don’t need it.

## Enable Message Content Intent

## Go to Discord Developer Portal
## 

## Select your bot TestB0T.

## Go to Bot → scroll to Privileged Gateway Intents.

## Turn on Message Content Intent.

## Save changes.


## Check the bot’s role permissions

## In your Discord server → right-click the server name → Server Settings → Roles.

## Find your bot’s role (should be named like “TestB0T”).

## Make sure it has View Channel and Send Messages for that specific channel.

## Also, check the channel’s own settings:

## Right-click the channel → Edit Channel → Permissions → ensure your bot’s role is allowed.


import discord
from discord.ext import tasks, commands
from datetime import datetime, time, timedelta
import asyncio

# --- CONFIG ---
TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = your_channel_id  # Replace with your real channel ID

clients = [
    {"name": "John", "end_date": "2025-12-10"},
    {"name": "Mia", "end_date": "2025-12-15"},
    {"name": "Luca", "end_date": "2025-12-07"}
]

intents = discord.Intents.default()  # no privileged intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    send_daily_reminder.start()

async def send_reminders():
    channel = await bot.fetch_channel(CHANNEL_ID)
    today = datetime.now().date()

    for client in clients:
        end_date = datetime.strptime(client["end_date"], "%Y-%m-%d").date()
        days_left = (end_date - today).days

        if days_left in [3, 4]:
            await channel.send(f"Hey {client['name']}, only {days_left} days remain until payment is due!")

@tasks.loop(hours=24)
async def send_daily_reminder():
    now = datetime.now()
    target_time = time(18, 27)  # 6:25 PM
    run_time = datetime.combine(now.date(), target_time)

    if now > run_time:
        run_time += timedelta(days=1)

    wait_seconds = (run_time - now).total_seconds()
    print(f"Next reminder in {wait_seconds / 60:.1f} minutes.")
    await asyncio.sleep(wait_seconds)

    await send_reminders()

bot.run(TOKEN)
