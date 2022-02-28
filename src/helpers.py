from os import system
from json import dumps, load
from colorama import Style, Fore, Back
from rfc3339 import rfc3339

def clearTerminal():
    system("clear||cls")

def askForWord(text):
    return input(text).upper()

def getWordOfDay(words, word_hash):
    return words[word_hash - 1].upper()

def printGrid(grid, is_keyboard = False):
    for i in range(len(grid)):
        if i > 0:
            print("\n")
        for j in range(len(grid[i])):
            if is_keyboard and len(grid[i][j]) == 1:
                print(colorText(grid[i][j], Back.WHITE), end = "  ")
            else:
                print(grid[i][j], end = "  ")
    print()

def getWordHash(today_date, hash_key):
    return today_date.timetuple().tm_yday - hash_key

def colorText(word, back, fore = Fore.BLACK):
    return back + fore + f" {word} " + Style.RESET_ALL

def colorKey(keyboard, index, plain_word, formatted_word, back = None, green = False):
    for row in range(len(keyboard)):
        for text in range(len(keyboard[row])):
            if green and back == None:
                if plain_word[index] in keyboard[row][text]:
                    keyboard[row][text] = formatted_word[index]
            else:
                if plain_word[index] in keyboard[row][text]:
                    if back not in keyboard[row][text]:
                        keyboard[row][text] = formatted_word[index]
    return keyboard

def normalizeWords(words):
    accents_equivalents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for i in range(len(words)):
        for accent in accents_equivalents.keys():
            words[i] = words[i].replace("\n", "").replace(accent, accents_equivalents[accent])
    return words

def saveWordOfDay(word, current_date, game_words_path):

    with open(game_words_path, 'r') as infile:

        formatted_date = current_date.strftime("%Y-%m-%d")
        word_details = {formatted_date: word}

        try:
            history = load(infile)
            history_dates = [list(x.keys())[0] for x in history]

            if not formatted_date in history_dates:
                history.append(word_details)
                with open(game_words_path, 'w') as infile:
                    infile.write(dumps(history, indent = 4))
        except:
            with open(game_words_path, 'w') as infile:
                infile.write(dumps([word_details], indent = 4))

def saveGameResult(word, current_date, result, attempts, game_history_path):

    with open(game_history_path, 'r') as infile:

        game_details = {rfc3339(current_date): word, "won": result, "attempts": attempts}

        try:
            history = load(infile)
            history.append(game_details)
            with open(game_history_path, 'w') as infile:
                infile.write(dumps(history, indent = 4))
        except:
            with open(game_history_path, 'w') as infile:
                infile.write(dumps([game_details], indent = 4))