import discord
import os
# import problem
from active_bot import active_bot
from discord.ext import commands
from discord import app_commands

class Bot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    super().__init__(command_prefix = "`", intents=intents)

  async def setup_hook(self):
    await self.tree.sync(guild = discord.Object(id=os.getenv('EBS')))
    print(f"synced slash commands for {self.user}")

  async def on_command_error(self, ctx, error):
    await ctx.reply(error, ephemeral = True)

  async def on_ready(self):
    print(f"We have logged in as {self.user.id}".format())

bot = Bot()

@bot.hybrid_command(name="hello", with_app_command = True, description = "hello")
@app_commands.guilds(discord.Object(id = os.getenv('EBS')))
async def hello(ctx: commands.Context):
  await ctx.defer(ephemeral = True)
  await ctx.reply(f"hello {ctx.message.author.mention}")

active_bot()
bot.run(str(os.getenv('KEY')))
