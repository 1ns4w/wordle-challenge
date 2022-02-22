from requests import get
from bs4 import BeautifulSoup

def getWords():
    page = get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    soup = BeautifulSoup(page.text, 'lxml')
    words = soup.find_all('td', class_='blob-code')
    for word in words:
        if len(word) == 5:
            print(word)

getWords()