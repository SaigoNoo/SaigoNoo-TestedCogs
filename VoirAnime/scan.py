from redbot.core import commands, Config
from requests import get
from bs4 import BeautifulSoup


class VoirAnime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.url_base = "https://v5.voiranime.com/?filter=subbed"

    @commands.command()
    async def voiranimelist(self, ctx):
        anime_list = self.scan()
        await ctx.send(f"{anime_list}")

    def get_datas(self, data) -> dict:
        """
        This method will collect all datas and create manually a dictionary of the available animes.
        :param data: Scrap of the main file.
        """
        output = {}
        for tag in data:
            temp = tag.find_all("a", class_="btn-link")
            anime_title = tag.find("a").text.strip()
            output[anime_title] = {}
            for element in temp:
                output[anime_title][element.text.strip()] = element["href"]
        return output

    def scan(self):
        """
        This method will simply scrap a webpage and get the HTML structure.
        """
        scrap = get(self.url_base)
        soup = BeautifulSoup(scrap.content, 'html.parser')
        result = soup.find_all(class_=["item-summary"])
        datas = self.get_datas(data=result)
        return datas
