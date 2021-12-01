import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com')

if r.status_code == 200:
	soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    
    for headline in soup.find_all("span", {"class": "mw-headline"}):
        print(headline.text)
        
