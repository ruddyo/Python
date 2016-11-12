from bs4 import BeautifulSoup
import urllib
# r = urllib.urlopen('https://indianapolis.craigslist.org/search/apa?max_price=700&availabilityMode=0').read()
r = urllib.urlopen('https://indianapolis.craigslist.org/apa/5846927650.html').read()
soup = BeautifulSoup(r, "html.parser")
# print type(soup)
# print soup.prettify()[0:1000]
# letters = soup.find_all("li", class_="result-row")
letters = soup.find_all("section", id="postingbody")
# print soup
print letters

lobbying = {}
for element in letters:
	lobbying[element.a.get_text()] = {}


prefix = "indianapolis.craigslist.org"
# print prefix+letters[0].a["href"]
print letters
for element in letters:
    lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]

for element in letters:
    date = element.find(class_="result-date").get_text()
    lobbying[element.a.get_text()]["date"] = date

# for item in lobbying.keys():
	# print item + ": \n\t"+ "link: " +lobbying[item]["date"], lobbying[item]["link"]
