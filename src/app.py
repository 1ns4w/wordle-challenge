from datetime import datetime
from colorama import Back, init
from generator import getSpanishWords
from constants import MAX_GAME_ATTEMPTS, WORDS_LENGTH, REQUIRED_WORDS, HASH_KEY, GAME_WORDS_PATH, GAME_HISTORY_PATH
from helpers import clearTerminal, normalizeWords, printGrid, colorText, saveGameResult, getWordHash, getWordOfDay, askForWord, saveWordOfDay

def main():

    init()
    clearTerminal()

    print(f"Cargando...")
    try:
        words = normalizeWords(getSpanishWords(WORDS_LENGTH))
    except:
        clearTerminal()
        exit("Has interrumpido la carga de palabras.")

    clearTerminal()
    
    game_board = []
    game_attempts_counter = 0
    game_words = words[:REQUIRED_WORDS]
    game_keyboard = [['Q'], ['A'], ['Z']]

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
            
            if game_attempts_counter > 0:
                print()
            answer = askForWord("Ingresa una palabra: ")

            while " " in answer or not (answer.lower() in words) or len(answer) != WORDS_LENGTH:
                print(f"Error: Ingresa una palabra válida de {WORDS_LENGTH} letras sin espacios.")
                answer = askForWord("Intenta nuevamente: ")

            answer_chars = list(answer)
            clearTerminal()
            
            for i in range(len(day_word)):
                if answer_chars[i] == day_word[i]:
                    answer_chars[i] = colorText(answer_chars[i], Back.GREEN)
                elif answer_chars[i] in day_word and not colorText(answer_chars[i], Back.YELLOW) in answer_chars:
                    answer_chars[i] = colorText(answer_chars[i], Back.YELLOW)
                else:
                    answer_chars[i] = colorText(answer_chars[i], Back.WHITE)

            game_board.append(answer_chars)
            printGrid(game_board)

            game_attempts_counter += 1

            if answer == day_word:
                saveGameResult(day_word, today_date, True, game_attempts_counter, GAME_HISTORY_PATH)
                print("\nGanaste.\n")
                break

            if game_attempts_counter == MAX_GAME_ATTEMPTS:
                saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
                print("\nPerdiste.\n")
    except:
        saveGameResult(day_word, today_date, False, game_attempts_counter, GAME_HISTORY_PATH)
        clearTerminal()
        exit("Has interrumpido el juego.")

if __name__ == "__main__":
    main()