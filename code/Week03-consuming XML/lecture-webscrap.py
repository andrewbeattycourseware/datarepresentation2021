import requests
from bs4 import BeautifulSoup

url = 'https://www.property.ie/property-for-sale/mayo/'
page = requests.get(url)
#print(page)
soup =BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

listings = soup.find_all("div", class_="search_result")
#print(listings[0])
for listing in listings:
    pricediv = listing.find("div", class_="sresult_description").find("h3").text
    print(pricediv)
    print("------------------")



