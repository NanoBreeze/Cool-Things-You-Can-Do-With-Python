'''
Copyright 2017 Linyi Cheng

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


from urllib.request import urlopen #used to get the HTML of a webpage
from bs4 import BeautifulSoup #used to parse html and look for specific elements

if __name__ == '__main__':
    wikiHtml = urlopen("https://en.wikipedia.org/wiki/Web_scraping") #gets HTML from wikipedia page
    bsInstance = BeautifulSoup(wikiHtml.read(), "html.parser") #formats the HTML so that it's easy to find specific elements
    hyperlinkTags = bsInstance.find_all("a")

    print("In total, " + str(len(hyperlinkTags)) + " hyperlink tags were found.")
    for hyperlinkTag in hyperlinkTags:
        print(hyperlinkTag.get("href"))



