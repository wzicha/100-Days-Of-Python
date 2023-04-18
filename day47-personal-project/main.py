import requests
from bs4 import BeautifulSoup

# send a request to the website
#url
response = requests.get(url)

# parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# locate all listings with the specified class
listings = soup.select('tr.tr-desktop.posting-row.posting-not-available, tr.tr-desktop.posting-row.posting-not-available.posting-verified')

# extract the relevant information from each listing
for listing in listings:
    # extract the price, date range, and view information
    price = listing.find('td', {'class': 'listing-price'}).text.strip()
    date_range = listing.find('span', {'class': 'long'}).text.strip()
    view = listing.find('td', {'class': 'listing-view'}).text.strip()

    # print the extracted information
    print(f'Price: {price}')
    print(f'Date Range: {date_range}')
    print(f'{view}')
