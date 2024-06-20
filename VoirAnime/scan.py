from redbot.core import commands, Config
from requests import get
from bs4 import BeautifulSoup


class VoirAnime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.list = self.get_datas()
        self.url_base = "https://v5.voiranime.com/?filter=subbed"

    @commands.command()
    async def voiranimelist(self, ctx):
        await ctx.send(f"{self.scan()}")

    @staticmethod
    def get_datas(data: object) -> dict:
        """
        This method will collect all datas and create manually a dictionary of the available animes.
        :param data: Scrap of the main file.
        """
        output = {}
        for tag in data:
            temp = tag.find_all("a", class_="btn-link")
            output[tag.find("a").text] = {}
            for element in temp:
                output[tag.find("a").text][element.text.strip()] = element["href"]
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
