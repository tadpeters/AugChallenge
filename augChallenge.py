import os
import requests
import datetime
from bs4 import BeautifulSoup

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
# print (titleString)

mydate = datetime.datetime.now()
# print (mydate)
modTime = '{:%m/%d/%Y %H:%M:%S}'.format(mydate)
# print (modTime)
# modTime = time for file writing

# pornStarName for writing to file
pornStarName = 'Fritz von Richthofen Helena'
# print (pornStarName)


# slicing for filename
domainOnly =  url.split('/')
filterDomainOnly = domainOnly[0].split('.')
if filterDomainOnly[-1] == 'org' or 'com':
	# print (filterDomainOnly[-2])
	ofilename = filterDomainOnly[-2]

os.chdir('.\datafolder')
with open(ofilename + '.txt', 'w') as f:
	answer = '%s\n%s\n%s\n%s' % (fcontents, titleString, modTime, pornStarName)
	f.write(answer) 
	# f.write(titleString + '\n')
	# f.write(modTime + '\n')
	# f.write(pornStarName)
	f.close()