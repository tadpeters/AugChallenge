import os
from bs4 import BeautifulSoup
import requests
import datetime
'''
open a file that has contains a website path, but it lacks the protocol example: google.com, not http://google.com				check
extract the title of the page from the meta data provided in the page, the stuff between the tag <title></title>				check
write that title in a new file called website name minus the protocol or any additional path information (example: google)
 the file contents should be the full path (take special note here, you might not get a top of domain page)
 the title of the page
 the time of the of the writing of the data in day/month/year 24:00:00 (no .seconds and year can be 2 or 4 digits, your choice)
 lastly your porn star name (name of your childhood pet + street you grew up on) or just your name.
'''

#reads file for url
for file in os.listdir('.\datafolder'):
	with open('./datafolder/' + file, 'r') as f:
		fcontents = f.read()
		# print (fcontents)
		# fcontents = needs to be sliced to use as ofilename
		url = fcontents

#prints title string for writing
response = requests.get('http://' + url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
titleString = soup.title.string

print (titleString)


mydate = datetime.datetime.now()
print (mydate)
modTime = '{:%m/%d/%Y %H:%M:%S}'.format(mydate)
# print (modTime)
# modTime = time for file writing


