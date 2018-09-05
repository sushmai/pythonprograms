import requests
from bs4 import BeautifulSoup

def getPortions(soup):
    heading = soup.find('div', {'class':'deck'})
    if heading:
        yield heading.text

    for p in soup.find_all('p', {'class':""}):
        yield p.text

def readPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    for element in getPortions(soup):
        f = open("yc.txt", "w")
        f.write(str("\n%s" % element))
        print("\n%s" % element)
        #print("\n%s" % element)
        #input("\n Press 'Enter ' to continue:")

    print('\nEnd of artical')

if __name__ == '__main__':
    url = "https://www.datacenterdynamics.com/news/microsoft-azure-suffers-outage-after-cooling-issue/"
    readPage(url)
