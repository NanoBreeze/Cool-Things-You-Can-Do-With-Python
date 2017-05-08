
from urllib.request import urlopen #used to get the HTML of a webpage
from bs4 import BeautifulSoup #used to parse html and look for specific elements

if __name__ == '__main__':
    wikiHtml = urlopen("https://en.wikipedia.org/wiki/Web_scraping") #gets HTML from wikipedia page
    bsInstance = BeautifulSoup(wikiHtml.read(), "html.parser") #formats the HTML so that it's easy to find specific elements
    hyperlinkTags = bsInstance.find_all("a")

    print("In total, " + str(len(hyperlinkTags)) + " hyperlink tags were found.")
    for hyperlinkTag in hyperlinkTags:
        print(hyperlinkTag.get("href"))



