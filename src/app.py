from os import path, stat
from datetime import datetime
from colorama import Back, init
from generator import getSpanishWords
from constants import MAX_GAME_ATTEMPTS, WORDS_LENGTH, REQUIRED_WORDS, HASH_KEY, WORDS_PATH, GAME_WORDS_PATH, GAME_HISTORY_PATH
from helpers import clearTerminal, normalizeWords, printGrid, colorText, saveGameResult, getWordHash, getWordOfDay, askForWord, saveWordOfDay, colorKey

def main():

    init()
    clearTerminal()

    if path.exists(WORDS_PATH) == False or stat(WORDS_PATH).st_size == 0:
        print(f"Cargando...")
        try:
            words = normalizeWords(getSpanishWords(WORDS_LENGTH))
        except:
            clearTerminal()
            exit("Has interrumpido la carga de palabras.")
    else:
        with open(WORDS_PATH, 'r') as infile:
            words = normalizeWords(infile.readlines())

    clearTerminal()
    
    game_board = []
    game_attempts_counter = 0
    game_words = words[:REQUIRED_WORDS]
    game_keyboard = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]

    """
    for row in range(len(game_keyboard)):
        for letter in range(len(game_keyboard[row])):
            game_keyboard[row][letter] = colorText(game_keyboard[row][letter], Back.WHITE)
    """

    today_date = datetime.now()
    word_hash = getWordHash(today_date, HASH_KEY)

    day_word = getWordOfDay(game_words, word_hash)
    saveWordOfDay(day_word, today_date, GAME_WORDS_PATH)

    try:
        while game_attempts_counter < MAX_GAME_ATTEMPTS:

            today_date = datetime.now()
            word_hash_check = getWordHash(today_date, HASH_KEY)

            if word_hash_check != word_hash:
                clearTerminal()
                game_board = []
                game_attempts_counter = 0
                day_word = getWordOfDay(game_words, word_hash_check)
                saveWordOfDay(day_word, today_date, GAME_WORDS_PATH)
                saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
                print("La palabra ha cambiado, el juego se ha reiniciado.")
                continue
            
            if game_attempts_counter == 0:
                print("KEYBOARD:\n")
                printGrid(game_keyboard, is_keyboard = True)
                print()

            answer = askForWord("Ingresa una palabra: ")

            while " " in answer or not (answer.lower() in words) or len(answer) != WORDS_LENGTH:
                print(f"Error: Ingresa una palabra válida de {WORDS_LENGTH} letras sin espacios.")
                answer = askForWord("Intenta nuevamente: ")
                print()

            answer_chars = list(answer)
            clearTerminal()
            
            for i in range(len(day_word)):

                if answer[i] == day_word[i]:
                    answer_chars[i] = colorText(answer_chars[i], Back.GREEN)
                    game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i], green = True)

                elif answer[i] in day_word and answer_chars.count(colorText(answer[i], Back.GREEN)) != day_word.count(answer[i]):
                    
                    if colorText(answer[i], Back.YELLOW) in answer_chars:
                        game_keyboard = colorKey(game_keyboard, answer[i], colorText(answer_chars[i], Back.YELLOW))
                        answer_chars[i] = colorText(answer_chars[i], Back.RED)
                    else:
                        answer_chars[i] = colorText(answer_chars[i], Back.YELLOW)
                        game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i])

                else:
                    answer_chars[i] = colorText(answer_chars[i], Back.RED)
                    game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i])

            print("GRID:\n")
            game_board.append(answer_chars)
            printGrid(game_board)
            print("\nKEYBOARD:\n")
            printGrid(game_keyboard, is_keyboard = True)
            print()

            game_attempts_counter += 1

            if answer == day_word:
                saveGameResult(day_word, today_date, True, game_attempts_counter, GAME_HISTORY_PATH)
                print("Ganaste.\n")
                break

            if game_attempts_counter == MAX_GAME_ATTEMPTS:
                saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
                print("Perdiste.\n")
    except:
        saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
        clearTerminal()
        exit("Has interrumpido el juego.")

if __name__ == "__main__":
    main()