import csv
import re
import requests
from bs4 import BeautifulSoup
from lib.lib import getURLs,format_Date

urls = getURLs()
print("Loading ...")
i = 1
for url in urls:
	#j = i + 1
	print("Writing file ("+str(i)+"/"+str(len(urls))+")")
	f = open("data/content_txt/"+str(i)+".txt","w")
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	content = soup.find("div", {"id": "ARTICLE_DETAILS"}).getText().replace('\n', ' ').replace('\r', '')
	f.write(content)
	f.close()
	i+=1
print("Done")
