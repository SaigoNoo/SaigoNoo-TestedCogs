from redbot.core import commands

class MusicBrainz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def piping(self, ctx):
        await ctx.send("Pong !")