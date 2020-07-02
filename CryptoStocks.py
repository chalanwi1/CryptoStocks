# import libraries needed for script
from bs4 import BeautifulSoup
import requests
import pandas

# create variable to store full urls of web pages to be scraped
urls = ['https://finance.yahoo.com/cryptocurrencies?offset=0&count=100',
        'https://finance.yahoo.com/cryptocurrencies?count=100&offset=100']

# create empty list to store scraped data
stocks = []

# loop through each url in urls list to scrape each page
for url in urls:
    
    # send request to url for response
    page = requests.get(url)

    # parse content of web page
    soup = BeautifulSoup(page.content, 'lxml')

    # select table  
    table = soup.find('table')

    # use pandas to read table from web page
    df = pandas.read_html(str(table))
    
    # append each table to stocks list
    stocks.append(df)

# use pandas to join tables together (concatenate) / ignore index numbers for each table   
result = pandas.concat([stocks[0][0], stocks[1][0]], ignore_index=True)

# delete undesired data points from table 
del result['52 Week Range']
del result['1 Day Chart']

# write scraped data to csv file 
result.to_csv('CryptoStocks.csv')

