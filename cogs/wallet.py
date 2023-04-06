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
class Wallet(commands.Cog, name="wallet"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="wallet",
        description="wallet [currency]",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    async def testcommand(self, context: Context, currency: str):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Create an embed object
        data = pyexhange.handle_command(f"wallet {context.author.id} {currency}")

        if data['status'] == "success":
            embed = discord.Embed(
                title=f"Wallet",
                color=discord.Color.gold()
            )
            # Add fields to the embed
            embed.add_field(name=f"{data['currency']}", value=f"{data['amount']}", inline=False)

            # Send the embed as a response to the command
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Failed",
                color=discord.Color.red(),
                description=f"{data['error']}"
            )
            # Send the embed as a response to the command
            await context.send(embed=embed)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Wallet(bot))
