import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import numpy as np

product_Names = []
Prices = []
shipping_info_list = []
product_subtitle_list = []

# Start a session to manage cookies and headers
session = requests.Session()
ua = UserAgent()

headers = {
    "User-Agent": ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.ebay.com/",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

cookies = {
    'nonsession': 'BAQAAAZRXz2gmAAaAADMABWl9iDE4OTExMADKACBrXruxYmFhYWQ3MDkxOTQwYWIxM2UxNTUxMzA4ZmZmZGI5MzMAywABZ5xbuTHcybmTsUleOB2iqlPkWDjuZaoEGg**',
    's': 'CgAD4ACBnnaYxYmFhYWQ3MDkxOTQwYWIxM2UxNTUxMzA4ZmZmZGI5MzMr8ELn',
    'dp1': 'bbl/US6b5ebbb1^',
    'ebay': '%5Esbf%3D%23000000%5E',
    'ns1': 'BAQAAAZRXz2gmAAaAANgAU2l9iDJjNjl8NjAxXjE3MzgyOTg1NDU5NzdeXjFeM3wyfDV8NHw3fDEwfDQyfDQzfDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3NeCo0/m8ofAW2fbRPYSh2+hxfRI4',
    '__uzma': '822c8ebb-b68a-43ac-800c-d6ea2161bd04',
    '__uzmb': '1738298545',
    '__uzmc': '326021057171',
    '__uzmd': '1738298545',
    '__uzme': '9089',
    '__uzmf': '7f6000e12baa4f-7594-414e-9bc9-0cfb3dfab44917382985459030-aa800c7bb6d6397010',
    'ak_bmsc': '2CF2CDC453C3ECCBE7A60064B4860425~000000000000000000000000000000~YAAQBXHKF1cWVaCUAQAAhdequhqcuIfsAa2rfRDxyX+i7surccaSS+1+W5sbVz0IeJJXXE80Jnb+3WK3OLBM2s6/R2s846NIydT7hCO6axeGK3RrNFzRZQJhs9esUu++va4bM4CIayGfHKiTwCTsfYdD9I3FhXfqBvMwrMe+BRddtnatqNIveA8tHwuqA+8zo4BsFt3SB6IsfAJMolnwnBvsZvfJVf6DLW5cr9ags+B8Yn8TWg8VnF+z6wHwZ9C2TKrO40h3j5eH3fEFQQuZjIIVYO5W/trC2k+5f49Vh40Jdo5EvRMm9Zy0wVPSntoqieEQCner9JheC25Ehz6sOk8scJZkffgO3RXsDnyID8MN/Tmix/FDr+rt'
}

session.headers.update(headers)

# Define the base URL for the eBay search
base_url = "https://www.ebay.com/sch/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&SSD%2520Capacity=2%2520TB&_nkw=laptops&_sacat=0"

# Send the first request to the base URL
response = session.get(base_url, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.content, 'html.parser')

# Parse product data and follow the "Next" button until it is no longer available
while True:
    # Find the product elements
    UL = soup.find("div", class_="srp-river-results clearfix")
    if not UL:
        print("No products found on this page. Exiting...")
        break
    
    page_list = UL.find("ul", class_="srp-results srp-list clearfix")
    product_elements = page_list.find_all("li", class_="s-item s-item__pl-on-bottom")
    
    # Parse product details
    for li in product_elements:
        product_Name = li.find('div', class_="s-item__title").span.text.strip() if li.find('div', class_="s-item__title") else np.nan
        product_Names.append(product_Name)

        subtitle_div = li.find('div', class_="s-item__subtitle")
        if subtitle_div:
            subtitle_span = subtitle_div.find('span')
            if subtitle_span:
                product_subtitle = subtitle_span.text.strip()
                product_subtitle_list.append(product_subtitle)
            else:
                product_subtitle_list.append(np.nan)
        else:
            product_subtitle_list.append(np.nan)

        product_price = li.find("div", class_="s-item__detail s-item__detail--primary").span.text.strip() if li.find("div", class_="s-item__detail s-item__detail--primary") else np.nan
        Prices.append(product_price)

        shipping_info_div = li.find("span", class_="s-item__shipping s-item__logisticsCost")
        if shipping_info_div:
            shipping_info = shipping_info_div.text.strip()
            shipping_info_list.append(shipping_info)
        else:
            shipping_info_list.append(np.nan)


    # Find the "Next" button and extract the URL
    next_button = soup.find("a", class_="pagination__next")
    if next_button and 'href' in next_button.attrs:
        next_page_url = next_button['href']
        print(f"Following next page: {next_page_url}")
        response = session.get(next_page_url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        print("No more pages found. Exiting...")
        break

# Ensure all lists have the same length
max_length = max(len(product_Names), len(Prices), len(shipping_info_list), len(product_subtitle_list))
product_Names.extend([np.nan] * (max_length - len(product_Names)))
Prices.extend([np.nan] * (max_length - len(Prices)))
shipping_info_list.extend([np.nan] * (max_length - len(shipping_info_list)))
product_subtitle_list.extend([np.nan] * (max_length - len(product_subtitle_list)))

# Create a DataFrame to store the scraped data
data = {
    'Product Name': product_Names,
    'Price': Prices,
    'Shipping Info': shipping_info_list,
    'Subtitle': product_subtitle_list,
}

df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('ebay_Data.csv', index=False)
print("Data saved to 'ebay_Data.csv'.")