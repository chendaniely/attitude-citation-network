import requests
from bs4 import BeautifulSoup

#
#
# get seed article
#
#

dave_2003_doi = "10.1.1.13.2424"
dave_2003 = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi=" + dave_2003_doi
print(dave_2003)


r = requests.get(dave_2003)
print(r)

data = r.text
soup = BeautifulSoup(data)

print(soup)

#
#
# get seed article citations by page
#
#

dave_2003_citing = "http://citeseerx.ist.psu.edu/showciting?doi=" + dave_2003_doi
dave_2003_r_citing = requests.get(dave_2003_citing)
print(dave_2003_r_citing)

data = dave_2003_r_citing.text
soup = BeautifulSoup(data)

#
#
# get seed article citation results
#
#
page2 = "http://citeseerx.ist.psu.edu/showciting?doi=10.1.1.13.2424&sort=cite&start=10"
print(page2)

print(soup)

results = soup.find_all('div', class_='result')

result = results[0]
