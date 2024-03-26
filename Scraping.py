import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://notebookspec.com/topchart/notebook.html"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
notebook = soup.find('ul', class_="top-100-list").find_all('li')

rankls = []
namels = []
pricels = []

for i in notebook:
    rank = i.find('div', class_='num').text 
    name = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text
    rankls.append(rank)
    namels.append(name)
    pricels.append(price)

df = pd.DataFrame({'list': rankls, 'name': namels, 'price': pricels})
df.to_excel('TopNotebook.xlsx')


# exporT iT xlsX #
