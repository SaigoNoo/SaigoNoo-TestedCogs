from .scan import VoirAnime


async def setup(bot):
    await bot.add_cog(VoirAnime(bot))
