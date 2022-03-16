import requests
import sys
import re
from textblob import TextBlob
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def crawl_miner(url,output,deep,range):
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        return
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        extract_text(output,soup,range)
        
        for links in soup.find_all(href=True):
            #print(links['href'])
            if deep>0 and re.match(regex, links['href']) is not None == True:
                deep = deep - 1
                crawl_miner(links['href'],output,deep,range)

def extract_text(output,soup,range):
    for headline in soup.find_all("h1"):
        for item in headline.text.strip().split():
            output.add(item)
    for headline2 in soup.find_all("h2"):
        for item in headline2.text.strip().split():
            output.add(item)
    if range > 1 : 
        title = soup.find("meta",property="of:title")
        if title:
            output.add(title)
    if range > 2:
        for ptag in soup.find_all("p"):
            for item in ptag.text.strip().split():
                output.add(item)
        for spantag in soup.find_all("span"):
            for item in spantag.text.strip().split():
                output.add(item)
        for litag in soup.find_all("li"):
            for item in litag.text.strip().split():
                output.add(item)

output = set()
url = sys.argv[1]
if url.startswith("http") == False:
    url = "https://"+url
deep = 1 # sys.argv[2]
range = 3 # sys.argv[3]
crawl = crawl_miner(url,output,deep,range)
words = set()
for txt in output:
    blob = TextBlob(txt)
    for word,pos in blob.tags:
        test = re.sub(r'[^a-zA-Z0-9_]', '', word)
        if  test and pos == 'NN' or pos == 'NNS': 
            words.add(test.lower())
            
print(words)
