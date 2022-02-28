from os import path, stat
from datetime import datetime
from colorama import Back, init
from generator import getSpanishWords
from constants import MAX_GAME_ATTEMPTS, WORDS_LENGTH, WORDS_PATH, REQUIRED_WORDS, HASH_KEY, GAME_WORDS_PATH, GAME_HISTORY_PATH
from helpers import clearTerminal, normalizeWords, printGrid, colorText, saveGameResult, getWordHash, getWordOfDay, askForWord, saveWordOfDay, colorKey, printSummary, printGuide

def main():

    init()
    clearTerminal()

    if path.exists(WORDS_PATH) == False or stat(WORDS_PATH).st_size == 0:
        print("Cargando palabras...")
        try:
            getSpanishWords(WORDS_LENGTH, outfile_path = WORDS_PATH)
            with open(WORDS_PATH, 'r') as infile:
                words = normalizeWords(infile.readlines())
        except:
            clearTerminal()
            exit("Has interrumpido la carga de palabras.")
    else:
        with open(WORDS_PATH, 'r') as infile:
            words = normalizeWords(infile.readlines())
    
    clearTerminal()
            
    game_attempts_counter = 0
    game_words = words[:REQUIRED_WORDS]
    game_board = [[" "] * WORDS_LENGTH] * MAX_GAME_ATTEMPTS
    game_keyboard = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]

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
                game_board = [[" "] * WORDS_LENGTH] * MAX_GAME_ATTEMPTS
                game_attempts_counter = 0
                day_word = getWordOfDay(game_words, word_hash_check)
                saveWordOfDay(day_word, today_date, GAME_WORDS_PATH)
                saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
                print("La palabra ha cambiado, el juego se ha reiniciado.")
                continue

            if game_attempts_counter == 0:
                print("WORDLE CLI:\n")
                printGrid(game_board)
                print("GUIDE:\n")
                printGuide()

            answer = askForWord("Ingresa una palabra: ")

            while " " in answer or not (answer.lower() in words) or len(answer) != WORDS_LENGTH:
                print(f"Error: Ingresa una palabra válida de {WORDS_LENGTH} letras sin espacios.\n")
                answer = askForWord("Intenta nuevamente: ")

            answer_chars = list(answer)
            clearTerminal()
            
            for i in range(len(day_word)):

                if answer[i] == day_word[i]:
                    answer_chars[i] = colorText(answer_chars[i], Back.GREEN)
                    game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i], green = True)

                elif answer[i] in day_word and day_word.count(answer[i]) != answer_chars.count(colorText(answer[i], Back.GREEN)) and answer_chars.count(colorText(answer[i], Back.YELLOW)) != 1:
                    answer_chars[i] = colorText(answer_chars[i], Back.YELLOW)
                    game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i])

                else:
                    answer_chars[i] = colorText(answer_chars[i], Back.RED)
                    if answer_chars.count(colorText(answer[i], Back.YELLOW)) == 0:
                        game_keyboard = colorKey(game_keyboard, answer[i], answer_chars[i])

            game_board[game_attempts_counter] = answer_chars

            print("WORDLE CLI:\n")
            printGrid(game_board)
            print("KEYBOARD:\n")
            printGrid(game_keyboard, is_keyboard = True)

            game_attempts_counter += 1

            if answer == day_word:
                saveGameResult(day_word, today_date, True, game_attempts_counter, GAME_HISTORY_PATH)
                clearTerminal(5)
                print("SUMMARY:\n")
                printSummary(game_board)
                break

            if game_attempts_counter == MAX_GAME_ATTEMPTS:
                saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
                clearTerminal(5)
                print("SUMMARY:\n")
                printSummary(game_board)
    except:
        saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
        clearTerminal()
        exit("Has interrumpido el juego.")

if __name__ == "__main__":
    main()