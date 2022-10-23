import requests
from bs4 import BeautifulSoup as bs


def parser(url):
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    quotes = soup.select('div.field-item.even.last > p')
    return [q.text.replace('\xa0', ' ').replace('\n', ' ') for q in quotes]