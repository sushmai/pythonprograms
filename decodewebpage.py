# request library to load HTML of the page
import requests

#beautiful soup to process HTML
from bs4 import BeautifulSoup

# request New york times home page
# supply URL 
url = 'http://www.nytimes.com'
# make aget request (r - all the information from page)
r = requests.get(url)

# specify what you looking for 
soup = BeautifulSoup(r.text,"html.parser")
headings = soup.findAll("h2", {"class": "story-heading"})

for heading in headings:
    if heading.findAll("a"):
        # .strip() removes leading/trailing whitespace
        print(heading.a.text.strip())
    else:
        print(heading.text)
