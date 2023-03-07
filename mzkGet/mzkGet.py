from redbot.core import commands
from discord import embeds

class MusicBrainz(commands.Cog):
    """Call some main functions with MusicBrainz"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mzkgetset(self, ctx):
        """Configure your mzkGet cog"""
        await ctx.send("Setting !")

    @commands.command()
    async def mzkget(self, ctx):
        """Search for a album or a single with title or MusicBrainz ID"""
        await ctx.send("Pong !")