import pandas as pd
import requests
from bs4 import BeautifulSoup

url_template = 'https://www.amazon.in/s?k=shoes&page={}&ref=sr_pg_2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}



brands = []
prices = []
titles = []


for page in range(1,8):
    url=url_template.format(page)
    resp = requests.get(url_template, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')

    for product in soup.find_all('div', {'data-component-type': 's-search-result'}):

        try:
            title=product.find('span',{'class':'a-size-base-plus a-color-base a-text-normal'}).text.strip()
        except:
            title=''
        titles.append(title)

        try:
            brand=product.find('span',{'class':'a-size-base-plus a-color-base'}).text.strip()
        except:
            brand=''
        brands.append(brand)

        try:
            price=product.find('span',{'class':'a-price-whole'}).text.strip()
        except:
            price=''
        prices.append(price)



data = {'Title':titles,'Brand':brands,'prices':prices}
df = pd.DataFrame(data)

df['prices']=df['prices'].str.replace(',','')
df.drop_duplicates(subset='Title',keep='first',inplace=True)

df.to_csv(r'C:\Users\Dell\Downloads\shoeinfomodified3.csv',index=False)



print('done')










