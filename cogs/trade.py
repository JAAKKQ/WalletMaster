""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""
import discord
from discord.ext import commands
from discord.ext.commands import Context
import pyexhange
import json

from helpers import checks

# Here we name the cog and create a new class for the cog.
class Trade(commands.Cog, name="trade"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="trade",
        description="This is a testing command that does nothing.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    async def testcommand(self, context: Context, amount: float, currency: str):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Create an embed object
        data = pyexhange.handle_command(f"trade {context.author.id} {amount} {currency}")
        embed = discord.Embed(
            title="Trade",
            color=discord.Color.blue()
        )
        # Add fields to the embed
        embed.add_field(name="Currency", value=f"{data['currency']} {data['amount']}", inline=False)
        embed.add_field(name="Cost", value=data['cost'], inline=False)

        # Send the embed as a response to the command
        await context.send(embed=embed)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Trade(bot))
