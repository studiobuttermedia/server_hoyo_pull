import discord
from dotenv import load_dotenv
from discord import app_commands
# from discord.ext import commands
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 871644064385216613))
            self.synced = True
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game('Star Wrench'))
        print(f'Star Wrench Bot is Online!')

intents = discord.Intents.default()
intents.message_content = True

# This area is where the bot runs
client = MyClient()
tree = app_commands.CommandTree(client)
client.run(TOKEN) # type: ignore

@tree.command(name = "test", description = "Test command", guild = discord.Object(id = 871644064385216613))
async def self(interaction: discord.Interaction): # type: ignore
    await interaction.response.send_message("Test command works!") # , ephemeral = True)
