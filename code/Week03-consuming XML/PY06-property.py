import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.property.ie/property-for-sale/mayo/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


property_file = open('week03property.csv', mode='w')
property_writer = csv.writer(property_file, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="search_result")

for listing in listings:
    print(listing)
    entryList = []

    address = listing.find(class_="sresult_address").find("h2").find("a").text.strip()
    entryList.append(address)
    price = listing.find(class_="sresult_description").find("h3").text.strip()
    entryList.append(price)

    property_writer.writerow(entryList)
property_file.close()
