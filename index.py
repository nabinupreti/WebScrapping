import requests

from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

elements = soup.find_all(class_="country-name")

for element in elements:
    print(element.text)