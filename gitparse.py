from bs4 import BeautifulSoup
import requests
import random

HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]

HEADER = {'User-Agent': random.choice(HEADERS_LIST)}

def parsegit(url):
    #url = "https://github.com/saisyam/python-flask/blob/master/simple/app.py" 
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "lxml")
    div = soup.find_all("div", {"itemprop" : "text"})
    div[0].find('details').decompose()
    return str(div[0])