import requests

from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites"

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

h1_tag = soup.find('h1')

if h1_tag:
    print(h1_tag.text)
else:
    print("H1 not found")

# if response:
#     print("Connection Successful!!")
# else:
#     print("Connection Failed")