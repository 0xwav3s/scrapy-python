from bs4 import BeautifulSoup
import requests
import csv
import re

def getURLs():
	arr = []
	#e_url = 'https://www.thesaigontimes.vn/121624/Cuoc-cach-mang-dau-khi-da-phien.html'
	url = input("Your URL: ")
	arr.append(url)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	new_feeds = soup.findAll("a", {"class": "NOtherTitle"})
	for feed in new_feeds:
		ur = 'https://www.thesaigontimes.vn'+feed.get('href')
		arr.append(ur)
	return arr

def format_Date(date):
	x = date.split(",")
	dd = x[1].strip().split('/')
	return dd[2]+"-"+dd[1]+"-"+dd[0]+x[2]

with open('data.csv', 'w') as csv_file:
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
