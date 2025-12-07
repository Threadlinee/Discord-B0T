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
from datetime import datetime

# --- CONFIG ---
TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = 59250923850932  # your Discord channel ID

clients = [
    {"name": "User", "discord_id": 928309823095820952, "start_date": "2025-11-12", "end_date": "2025-12-12"},
    {"name": "User", "discord_id": 234567890123456789, "start_date": "2025-10-01", "end_date": "2025-11-01"},
    {"name": "User", "discord_id": 345678901234567890, "start_date": "2025-08-05", "end_date": "2026-02-05"},
]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    check_clients.start()  # start the loop

@tasks.loop(minutes=1)
async def check_clients():
    """Ping all clients with 5 days or less remaining every minute."""
    channel = await bot.fetch_channel(CHANNEL_ID)
    today = datetime.now().date()

    for client in clients:
        end_date = datetime.strptime(client["end_date"], "%Y-%m-%d").date()
        days_left = (end_date - today).days

        if 0 < days_left <= 5:
            await channel.send(
                f"Hey <@{client['discord_id']}>, {days_left} days remain until your payment is due! 💸"
            )

bot.run(TOKEN)
