from bs4 import BeautifulSoup
from lib.lib import getURLs,format_Date
import requests
import csv
import re

with open('data/csv/data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['URL','Title','Author','Date'])
	urls = getURLs()
	print("Loading ...")
	for url in urls:
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')
		title = soup.find("span", {"class": "m_Title"}).getText()
		author = soup.find("span", {"class": "m_ReferenceSourceTG"}).getText()
		author = re.sub('[()*!@#$]', '', author)	#Remove symbol
		author = author.strip()		#Remove white space begin and end
		date = soup.find("span", {"class": "Date"}).getText()
		date = format_Date(date)
		writer.writerow([url,title,author,date])
	print("Done")
