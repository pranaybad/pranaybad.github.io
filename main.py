# if you want to scrape a website:
#     1. usethe API
#     2.HTML Web SCraping some tool likE beautifull saup4

# step 0: install all  the req

# pip install requests
# pip install bs4
# pip install html5lib
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1: Get the html
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# step 2:parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# step 3:  html tree traversal

# commenly types of objects
# 1.tags
# 2.beautifillsoup
# 3.navigablestring

# 4.comment
markup ="<p><!--this is comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

# title = soup.title
# print(type(title.string))


# get the title of the html page
title = soup.title

# get all the paragrapgh from the page
# paras = soup.find_all('p')
# print(paras)



 #get first elements in the html page
# print(soup.find('p'))

 #get classes of any html elements in the html page
# print(soup.find('p')['class'])

# find all the elements withclass lead
# print(soup.find_all("p", class_="lead"))

# get the tex in the elements
print(soup.find("p").get_text())
print(soup.get_text())

# get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)
all_links = set()
# get all the link on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = 'https://codewithharry.com' +(link.get('href'))
        all_links.add(link)
        print(linkText)
    