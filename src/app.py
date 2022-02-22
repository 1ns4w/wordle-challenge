from colorama import Fore
import requests
from bs4 import BeautifulSoup


def getWords():
    page_request = requests.get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    page_dom = page_request.text
    soup = BeautifulSoup(page_dom, 'lxml')
    tags = soup.find('div')
    print(tags.prettify())



print(getWords())