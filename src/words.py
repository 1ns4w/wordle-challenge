from requests import get
from bs4 import BeautifulSoup

def getWordsOfLength(length):
    page = get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    soup = BeautifulSoup(page.text, 'lxml')
    words_tags = soup.find_all('td', class_='blob-code')
    with open(f'{length}LengthWords.txt', 'w') as file:
        for word_tag in words_tags:
            word = f'{word_tag.text}\n'
            if len(word) == length : file.write(word)

getWordsOfLength(8)