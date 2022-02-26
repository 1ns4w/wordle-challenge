from requests import get
from random import shuffle
from bs4 import BeautifulSoup

# writes to a file or returns an array of n words of length m
def getSpanishWords(words_length, total_words = None, outfile_path = None):

    page = get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    soup = BeautifulSoup(page.text, 'lxml')

    words_tags = soup.find_all('td', class_ = 'blob-code')
    words_tags_text = list(map(lambda word_tag: word_tag.text, words_tags))
    total_words = len(words_tags_text) if total_words > len(words_tags_text) or total_words == None else total_words

    words = []
    shuffle(words_tags_text)

    for word in words_tags_text:
        if len(word) == words_length:
            words.append(word)
        if len(words) == total_words:
            break

    if outfile_path != None:
        with open(outfile_path, 'w') as outfile:
            for word in words:
                outfile.write(word + '\n')
    else:
        return words

getSpanishWords(5, 365, "assets/palabras5.txt")