from .mzkGet import MusicBrainz

def setup(bot):
    bot.add_cog(MusicBrainz(bot))
