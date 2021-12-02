import requests
import sys
from bs4 import BeautifulSoup

def crawl_miner(url,output,deep):
        
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        for headline in soup.find_all("h1"):
            for item in headline.text.strip().split():
                output.add(item)
        for headline2 in soup.find_all("h2"):
            for item in headline2.text.strip().split():
                output.add(item)
        title = soup.find("meta",property="of:title")
        if title:
            output.add(title)
        
        for links in soup.find_all(href=True):
            #print(links['href'])
            if deep>0:
                deep = deep - 1
                crawl_miner(links['href'],output,deep)

output = set()
url = sys.argv[1]
deep = 2
crawl = crawl_miner(url,output,deep)

print(output)
