########################################################################################
##-Scraping Seinfeld Scripts from https://www.seinfeldscripts.com with BeautifulSoup--##
########################################################################################

##########################
##--importing packages--##
##########################

import requests
import re
from bs4 import BeautifulSoup

##################
##--user agent--##
##################

user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
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

links_list = []
eps_only = []

for link in soup.find_all('a'):
    links_list.append(link.get('href'))

#print(links_list)

### sorting for links that contain 'the' as each episode title contains the word 'the' ###

# for i in links_list:
#     if re.match('^The', i) is not None:
#         eps_only.append(i)

# print(eps_only)

### option 1 - works ###

# for link in links_list:
#          # Convert data types, or will be error
#     link = str(link)
#          # Regular expression to obtain the necessary data
#     if re.match('^The', link) is not None:
#          eps_only.append(link)
#          print(eps_only)

### option 2 - works ###

# for i in links_list:
#     if i is not None and re.match('^The', i) is not None:
#         eps_only.append(i)
#         print(eps_only)

### option 3 - doesn't work ###

for link in links_list:
    link = link.replace(' ', '')
    if link is not None and re.match('(The)', link) is not None:
        eps_only.append(link)
print(eps_only)