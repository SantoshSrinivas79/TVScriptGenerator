########################################################################################
##-Scraping Seinfeld Scripts from https://www.seinfeldscripts.com with BeautifulSoup--##
########################################################################################

## TODO: only print each page between '<p>Quotes and Scene summary:</p>' and '<p>[End]</p>' for each episode html
## or htm file. located within '<div id="content">'

##########################
##--importing packages--##
##########################

import unicodedata
import requests
import re
from bs4 import BeautifulSoup

##################
##--user agent--##
##################

user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 ' \
                     'Safari/537.36'

headers = {'User-Agent': user_agent_desktop}

#########################
##--fetching the page--##
#########################

URL = 'https://www.seinfeldscripts.com/seinfeld-scripts.html'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

############################################################
##--scraping the links to the scripts from the main page--##
############################################################

### scraping raw links e.g. 'TheSeinfeldChronicles.htm'
links_list = []

### appending links to url e.g. 'https://www.seinfeldscripts.com/TheSeinfeldChronicles.htm'
script_links = []

# ## scraping links that direct to subpages that contain scripts ex.
# 'https://www.seinfeldscripts.com/TheSeinfeldChronicles.htm'
eps_only = []

### scraping pure script html from subpages
eps_body_only = []

for link in soup.find_all('a'):
    links_list.append(link.get('href'))

### appending '.html' and '.htm' links to website url ###

for link in links_list:
    if link is not None:
        link = link.replace(' ', '')
        script_links.append(f'https://www.seinfeldscripts.com/{link}')

### sorting for links that contain 'the' as each episode title contains the word 'the' ###

for link in script_links:
    if link is not None and re.search('\W*(The)\W*', link) is not None:
        eps_only.append(link)

############################################
##--scraping html from the list of links--##
############################################

### create a function that collects the soups for each subpage ###

for link in eps_only:
    r = requests.get(link, headers=headers)
    r.encoding = 'utf-8'

    script_content = r.text
    big_soup = BeautifulSoup(script_content, 'lxml')
    container = big_soup.find('div', id='content')
    for n in container.find_all('p', recursive=False):
        eps_body_only.append(n.text)

str1 = ''.join(eps_body_only)
str2 = unicodedata.normalize("NFKD", str1)

######################
##--saving to .txt--##
######################

# with open('complete_seinfeld_scripts.txt', 'w') as file:
#     file.write(str2)

#######################
##--saving to .JSON--##
#######################

import json

with open('complete_seinfeld_scripts.json', 'w', encoding='utf-8') as f:
    json.dumps(f, ensure_ascii=False, indent=4)
