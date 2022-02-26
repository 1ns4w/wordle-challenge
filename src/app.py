from colorama import Fore
import sys, platform, os
from datetime import datetime

def main():

    INFILE_PATH = 'assets/palabras5.txt'
    infile = open(INFILE_PATH, 'r')
    words = lineBreakSeparatedValuesToArray(infile.read())
    normalized_words = normalize_words(words)

    GAME_ATTEMPTS = 5
    day_of_year = int(datetime.now().strftime('%j'))
    day_word = normalized_words[day_of_year - 1]
    
def normalize_words(words):
    accents_equivalents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for i in range(len(words)):
        for accent in accents_equivalents.keys():
            words[i] = words[i].replace(accent, accents_equivalents[accent])
    return words

def lineBreakSeparatedValuesToArray(text):
    return text.split('\n')[:-1]

if __name__ == "__main__":
    main()

