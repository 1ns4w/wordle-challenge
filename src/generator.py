import requests
from bs4 import BeautifulSoup

# writes to a file or returns an array of n words of length m
def getSpanishWords(words_length, outfile_path = None, total_words = None):

    page = requests.get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    soup = BeautifulSoup(page.text, 'lxml')

    words_tags = soup.find_all('td', class_ = 'blob-code')
    words_tags_text = list(map(lambda word_tag: word_tag.text, words_tags))
    words = list(filter(lambda word: len(word) == words_length, words_tags_text))

    if outfile_path != None:
        with open(outfile_path, 'w') as outfile:
            for index in range(len(words) if total_words == None or total_words > len(words) else total_words):
                outfile.write(words[index] + '\n')
    else:
        return words
