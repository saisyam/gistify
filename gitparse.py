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

def parsegit(url, lineno): 
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "lxml")
    div = soup.find_all("div", {"itemprop" : "text"})
    div[0].find('details').decompose()
    
    if lineno is not None:
        trs = div[0].find_all('tr')
        # split line by comma separated
        # 1,5 - display 1 and 5 lines
        # 1,3-5,8 - display 1,3,4,5 and 8 lines
        vlines = linestodisplay(lineno, len(trs))
        index = 1
        for tr in trs:
            if index not in vlines:
                tr.decompose()
            index = index + 1

    return str(div[0])

def linestodisplay(linestring, maxlines):
    lines = linestring.split(",")
    vlines = []
    for line in lines:
        #find if there is any range
        rlines = line.split("-")
        if len(rlines) > 1:
            vlines.extend(range(int(rlines[0]), int(rlines[1])))
            vlines.append(int(rlines[1]))
        else:
            vlines.append(int(rlines[0]))
    vlines.sort()
    while vlines[-1] > int(maxlines):
        vlines.remove(vlines[-1])
    return vlines

def github_contribution(url):
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "lxml")
    div = soup.find("div", {"class": "js-yearly-contributions"})
    details = soup.find("details")
    if details is not None:
        details.decompose()
    footer = soup.find("div", {"class": "contrib-footer"})
    if footer is not None:
        tdiv = footer.find_all("div")
        if tdiv is not None:
            tdiv[0].decompose()
    return str(div)