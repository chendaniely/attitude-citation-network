import requests
from bs4 import BeautifulSoup

dave_2003_doi = "10.1.1.13.2424"
dave_2003 = "http://citeseerx.ist.psu.edu/viewdoc/summary?doi=" + dave_2003_doi
print(dave_2003)


r  = requests.get(dave_2003)
