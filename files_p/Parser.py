from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

url = 'https://www.imdb.com/chart/top/'
ua = UserAgent ()
rand_ua = ua.random
connecting = {'User-Agent': rand_ua}
page = requests.get(url, headers=connecting)

def parse():
    Rang = {}
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        film = soup.findAll('div', class_='ipc-metadata-list-summary-item__tc')
        for data in film:
            Names = data.find('h3', {'class': 'ipc-title__text'}).text
            Rangi = data.find('span', {'class': 'ipc-rating-star--imdb'}).text
            Rang[Names] = Rangi
        for i, j in Rang.items():
            print(i, " ", j)
    else:
        print(page.status_code, " - ошибка подключения")

