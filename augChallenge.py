import os
from bs4 import BeautifulSoup
import requests


#reads file for url
for file in os.listdir('.\datafolder'):
	with open('./datafolder/' + file, 'r') as f:
		fcontents = f.read()
		# print (fcontents)
		url = fcontents

#prints title string for writing
# url = "http://google.com"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
titleString = soup.title.string

print (titleString)


