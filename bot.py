# Please note that the application method used here is just an example, you're able to change it if you please.

import discord as disc
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=["-"], description="AQ3D Squad recruitment boat.")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Recruiting members"))
    print("Successfully connected to the socket.")

@bot.command()
async def info():
    await bot.say("This is the official recruitment bot for the AQ3D Squad Discord server.")

@bot.command()
async def template():
    await bot.say("1) Where did you find our server?")
    await bot.say("2) How long have you been a member?")
    await bot.say("3) Have you had any past experiance with server moderation?")
    await bot.say("4) How will you contribute towards the server itself?")
    await bot.say("5) Why do you want to become part of the staff team?")
    await bot.say("6) How old are you? Be truthful.")
    await bot.say("```Process has completed successfully, please DM an online member of staff with your application.```")
await bot.say(embed=embed)

@bot.command()
async def help():
    embed = discord.Embed(title="AQ3D Squad Recruiter Base", description="Here is a full list of my available commands.", color=0x00a0ea)
    embed.add_field(name="Information", value="info - Gives some basic information of the boat")
    embed.add_field(name="Recruitment", value="template - Gives you the servers staff application template")

token os.environ.get("DISCORD")
bot.run(f'{token}')