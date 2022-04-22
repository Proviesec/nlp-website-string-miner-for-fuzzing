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

# Find and Extract all url parameter from a big text
def extract_url(text):
    key_list = set()
    text = text.decode('utf-8')
    urls_extract = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    for url in urls_extract:
        params = re.findall(r'([^=&]+)=([^=&]+)', url)
        res = dict()
        for key, val in params:
            key_list.add(val)
    return key_list
      

def crawl_miner(url):
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        return
    if r.status_code == 200:
        return r.content
    else:
        return

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
deep = int(sys.argv[2]) # 1
range = int(sys.argv[3]) # 3
export = int(sys.argv[4]) # 0
crawl = crawl_miner(url)
if crawl:
    soup = BeautifulSoup(crawl, 'html.parser')
    extract_text(output,soup,range)
    if export == 1:
        for item in output:
            print(item)
    else:
        print(len(output))
words = set()

txt_return = extract_url(crawl)
for txt_url in txt_return:
    words.add(txt_url)

for txt in output:
    blob = TextBlob(txt)
    for word,pos in blob.tags:
        test = re.sub(r'[^a-zA-Z0-9_]', '', word)
        if  test and pos == 'NN' or pos == 'NNS': 
            words.add(test.lower())

if export:
    with open('name-miner-export.txt', 'w') as f:
        f.write(str(words))
            
print(words)
