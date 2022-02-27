from os import system
from json import dumps, load
from colorama import Style, init
from rfc3339 import rfc3339

def gameStart():
    init()
    clear()

def clear():
    system("clear||cls")

def askForWord(text):
    return input(text).upper()

def getWordOfDay(words, word_hash):
    return words[word_hash - 1].upper()

def print_colored_grid(grid):
    for i in range(len(grid)):
        if i > 0:
            print("\n")
        for j in range(len(grid[i])):
            print(grid[i][j], end = "  ")
    print()

def getWordHash(today_date, hash_key):
    return today_date.timetuple().tm_yday - hash_key

def style_text(word, back, fore):
    return back + fore + f" {word} " + Style.RESET_ALL

def normalize_words(words):
    accents_equivalents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for i in range(len(words)):
        for accent in accents_equivalents.keys():
            words[i] = words[i].replace(accent, accents_equivalents[accent])
    return words

def lineBreakSeparatedValuesToArray(text):
    return text.split("\n")[:-1] if text.split("\n")[-1] == '\n' else text.split("\n")

"""
def saveGameDetails(date, word, outfile_path):
    with open(outfile_path, 'w') as outfile:
        record = {str(date): word}
        outfile.write(dumps([record], indent = 4))
"""

def saveGameResult(word, current_date, result, tries, game_history_path):
    
    with open(game_history_path, 'r') as infile:

        game_details = {rfc3339(current_date): word, "result": result, "tries": tries}

        try:
            history = load(infile)
            history.append(game_details)
            with open(game_history_path, 'w') as infile:
                infile.write(dumps(history, indent = 4))
        except:
            with open(game_history_path, 'w') as infile:
                infile.write(dumps([game_details], indent = 4))

"""
def getGameDetails(date, word):
    return {str(date): word}

    infile = open(GAME_HISTORY_PATH, 'r')
    try:
        records = load(infile)
        records_dates = list(map(lambda record: record.keys()[0], records))
        if not today_date in records_dates:
            records.append(getGameDetails(rfc3339(today_date), day_word))
            infile = open(GAME_HISTORY_PATH, 'w')
            infile.write(dumps(records, indent = 4))
            infile.close()
    except:
        saveGameDetails(rfc3339(today_date), day_word, GAME_HISTORY_PATH)

"""