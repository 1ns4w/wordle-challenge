import requests
from bs4 import BeautifulSoup

# returns an array of words of length n or writes words of length n to a file
def getSpanishWords(words_length, outfile_name = None):
    page = requests.get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    soup = BeautifulSoup(page.text, 'lxml')
    words_tags = soup.find_all('td', class_ = 'blob-code')
    words = list(map(lambda word_tag: word_tag.text, words_tags))
    if outfile_name != None:
        with open(f"./words/{outfile_name}", 'w') as outfile:
            for word in words:
                if len(word) == words_length:
                    outfile.write(word + '\n')
    else:
        return list(filter(lambda word: len(word) == words_length, words))