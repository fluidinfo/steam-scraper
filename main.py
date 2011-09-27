#import scraperwiki
from BeautifulSoup import BeautifulSoup
import lxml.html
import re

# Blank Python

url = 'http://store.steampowered.com/search/?sort_by=&sort_order=ASC&page=%d'
url = 'http://store.steampowered.com/search/results?page=1'

with open("steam-1.html") as f:
#for i in range(2):
#    html = scraperwiki.scrape(url % (i + 1))
    html = f.read()
    bs = BeautifulSoup(html)

    for tag in bs.findAll(attrs={'class' : ['search_result_row odd', 'search_result_row even']}):
        price = tag.find('div', attrs={'class' : 'col search_price'}).contents
        itemType = tag.find('div', attrs={'class' : 'col search_type'}).contents
        metascore = tag.find('div', attrs={'class' : 'col search_metascore'}).contents
        released = tag.find('div', attrs={'class' : 'col search_released'}).contents
        capsule = tag.find('div', attrs={'class' : 'col search_capsule'}).contents
        name = tag.find('div', attrs={'class' : 'col search_name ellipsis'}).contents
 
        print name
    #for game in root.cssselect("a[class = 'search_result_row even' or class = 'search_result_row odd']"):
    #    titles = game.cssselect("div[class='col search_name ellipsis']")
    #    title = titles[0]
    #    print title.text_content()

    #    prices = game.cssselect("div[class='col search_price']")
    #    price = prices[0]
    #    print price.text_content()

