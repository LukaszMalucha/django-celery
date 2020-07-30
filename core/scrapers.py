import requests
from bs4 import BeautifulSoup

URL = "https://dev.to/search?q=django"




def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)
    return soup
