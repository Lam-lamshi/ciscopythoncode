import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://en.softonic.com/windows/trending.php?page="+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        features = "html.parser"
        for link in soup.findAll("a", {"class": "item_name"}):
            href = "http://en.softonic.com/"+link.get("href")
            #print(href)
            # print(title)
            get_single_item_date(href)
        page +=1
def get_single_item_date(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findALL("div",{"class":"i-name"}):
        print(item_name.string)

trade_spider(1)
