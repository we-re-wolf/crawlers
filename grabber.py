import requests
import re
from urllib.parse import urljoin

target_url = 'http://nmap.org/'
target_links = []

def grabber_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

def crawl(url):
    href = grabber_links(url)
    for link in href:
        link = urljoin(target_url, link)
        if '#' in link:
            link = link.split('#')[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)
        else:
            pass

crawl(target_url)