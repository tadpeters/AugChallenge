#!/usr/bin/env python

#import modules used here
import os
import datetime
#dependencies - bs4 is for py3+
import requests
from bs4 import BeautifulSoup

def readFile():
	''' reads file returns file contents (fcontents) '''
	for file in os.listdir('datafolder'):
		with open('./datafolder/' + file, 'r') as f:
			fcontents = f.read()
	f.close()
	return (fcontents)

def titleString(url):
	''' uses file contents (fcontents) to get title from webpage and returns titleString '''
	response = requests.get('http://' + url)
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	titleString = soup.title.string
	return (titleString)

def timeStamp():
	''' formats and returns mod time '''
	mydate = datetime.datetime.now()
	modTime = '{:%m/%d/%Y %H:%M:%S}'.format(mydate)
	return (modTime)

def ofile(url):
	''' filters file contents into domain only by splitting on /, then splitting on . '''
	domainOnly =  url.split('/')
	filterDomainOnly = domainOnly[0].split('.')
	ofilename = filterDomainOnly[-2]
	return (ofilename)

def bowchickabowwow():
	''' adds pets name to street name, returns pornStarName '''
	childhoodPetsName = 'Fritz von Richthofen'
	childhoodStreetName = 'Helena'
	pornStarName = (childhoodPetsName + ' ' + childhoodStreetName)
	return (pornStarName)

def main():
	''' writefile and call def's '''
	outfile = ofile(readFile())
	oreadFile = readFile()
	otitleString = titleString(readFile())
	otimeStamp = timeStamp()
	opornStarName = bowchickabowwow()
	with open('./datafolder/' + ofile(readFile()) + '.txt', 'w') as f:
		answer = '%s\n%s\n%s\n%s' % (oreadFile, otitleString, otimeStamp, opornStarName)
		f.write(answer) 
		f.close()
		
if __name__ == '__main__':
	main()
