import discord
from discord.ext import tasks, commands
from datetime import datetime

# --- CONFIG ---
TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = 1110  # replace with your channel ID

intents = discord.Intents.default()  # no privileged intents needed
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    send_every_minute.start()  # start the loop

async def send_message():
    channel = await bot.fetch_channel(CHANNEL_ID)
    now = datetime.now().strftime("%H:%M:%S")
    await channel.send(f"Hey! Current time is {now} ⏰")

@tasks.loop(minutes=1)  # runs every 1 minute
async def send_every_minute():
    await send_message()

bot.run(TOKEN)
