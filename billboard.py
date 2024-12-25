from bs4 import BeautifulSoup
import requests

class Billboard:
    def __init__(self):
        self.end_point = "https://www.billboard.com/charts/hot-100/"
        self.songs = []
    def scrape_songs(self,date):
        url = self.end_point + date
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        response = requests.get(url=url,headers=header)
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        songs_tags = soup.select("li.o-chart-results-list__item h3.c-title")# Correct class name might differ
        song_titles = []
        for song in songs_tags:
            song_titles.append(song.getText().strip())
        self.songs = song_titles
        return song_titles
