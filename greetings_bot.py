# If you scroll a little bit lower, you’ll see the actual switches labeled:

# PRESENCE INTENT

# SERVER MEMBERS INTENT

# MESSAGE CONTENT INTENT

# You just gotta flip the last two ON.

# Do this:

# Go to the Developer Portal → Applications → TestB0T → Bot tab.

# Scroll down to “Privileged Gateway Intents.”

# Turn on:

# ✅ SERVER MEMBERS INTENT (for greeting new members)

# ✅ MESSAGE CONTENT INTENT (stops that warning you keep seeing)

# Hit Save Changes at the bottom.

import discord
from discord.ext import commands

TOKEN = "YOUR_NEW_REGENERATED_TOKEN"
CHANNEL_ID = 523905983209582  # Replace with your real channel ID

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is None:
        channel = await bot.fetch_channel(CHANNEL_ID)
    await channel.send(f"Welcome to the server, {member.mention}! 🎉")

bot.run(TOKEN)
