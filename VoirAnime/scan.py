from redbot.core import commands


class VoirAnime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def voiranimeset(self, ctx):
        """This will do stuff"""
        await ctx.send(f"{type(self.bot)}")
