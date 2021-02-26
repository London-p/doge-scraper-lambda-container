
from bs4 import BeautifulSoup
import requests

try:
    url = "https://www.coindesk.com/price/dogecoin"
    req = requests.get(url)
    bsObj = BeautifulSoup(req.text, "html.parser")
    data = bsObj.find("div",class_ = "price-large").text
    print(data)

except: print("Site down")



