import discord
from discord.ext import commands
from random import randint
from random import choice
import random
import aiohttp
import asyncio
import os
from .utils import checks

"Made by StarBuck"

class War:
    "GUNS!"
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(no_pm=True, hidden=False)	
	
    async def shoot(self, user : discord.Member):
        """Shoots a user."""
        name = " *" + user.name + "*"        
        msg = "︻デ═一:collision: - - - - - - - " + name        
        await self.bot.say(msg)
		
    @commands.command(no_pm=True, hidden=False)	
	
    async def shell(self, user : discord.Member):
        """Shells a user."""
        name = " *" + ":fire:" + user.name + ":fire:" + "*"
        msg = "\n" + "           [-------]═════[o]:dash:                                            " + name + "\n" + ".- = = '= ' = = '-.                                                      " + "\n" + "(O_o_o_o_o_O)                                                 "
        await self.bot.say(msg)
		
    @commands.command(no_pm=True, hidden=False)
	
    async def rpg(self, user : discord.Member):
        """Fires RPG at user."""
        name = " *" + ":collision:" + user.name + ":collision:" + "*"
        msg = ":cloud:════════|:dash:----------------------------------" + name
        await self.bot.say(msg)
		
def setup(bot):
    n = War(bot)
    bot.add_cog(n)