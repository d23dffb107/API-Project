import urllib2
import json
from bs4 import BeautifulSoup

#Gets first paragraph from Wikipedia about the location
def getWiki(location):
    url1 = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&srlimit=1&format=json".format(location)
    result1 = json.loads(urllib2.urlopen(url1).read())
    place = result1['query']['search'][0]['title'].replace(" ", "%20")
    url2 = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&format=json".format(place)
    result2 = json.loads(urllib2.urlopen(url2).read())
    key = result2['query']['pages'].keys()[0]
    info = result2[u'query']['pages'][key]['extract']
    soup = BeautifulSoup(info, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text().encode("utf-8"))
    return paragraphs[0]


