
from bs4 import BeautifulSoup
import requests

url = "http://google.com"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
titleString = soup.title.string

print (titleString)
