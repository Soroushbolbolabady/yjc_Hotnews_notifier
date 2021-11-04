import notify2
import requests
from bs4 import BeautifulSoup
respons = requests.get("https://www.yjc.news/")
respons = respons.content
soup = BeautifulSoup(respons , "lxml")
items = soup.find_all("div" , {"class" , "subtitle-top-news-2"})
for item in items:
	item = item.get_text()
	notify2.init("News")

	n = notify2.Notification("Hot News",
							item,
							)
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.set_timeout(1000)
	n.show()
