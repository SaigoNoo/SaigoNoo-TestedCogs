from redbot.core import commands
from discord import embeds

class MusicBrainz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mzkgetset(self, ctx):
        await ctx.send("Setting !")

    @commands.command()
    async def mzkget(self, ctx):
        await ctx.send("Pong !")