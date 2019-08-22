from bs4 import BeautifulSoup
import requests

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
