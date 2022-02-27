from os import path, stat
from datetime import date
from json import loads, dumps
from colorama import Back, Fore
from generator import getSpanishWords
from constants import MAX_GAME_ATTEMPTS, WORDS_LENGTH, REQUIRED_WORDS, HASH_KEY, INFILE_PATH, GAME_HISTORY_PATH
from helpers import clear, normalize_words, print_colored_grid, style_text, lineBreakSeparatedValuesToArray, saveGameDetails, getWordHash, getWordOfDay, askForWord, gameStart

def main():

    gameStart()
    if path.exists(INFILE_PATH) == False or stat(INFILE_PATH).st_size == 0:
        print(f"Cargando...")
        words = normalize_words(getSpanishWords(WORDS_LENGTH))
    else:
        infile = open(INFILE_PATH, 'r')
        words = normalize_words(lineBreakSeparatedValuesToArray(infile.read()))
        infile.close()

    clear()
    
    game_board = []
    game_attempts_counter = 0
    game_words = words[:REQUIRED_WORDS]
    game_keyboard = [['Q'], ['A'], ['Z']]

    today_date = date.today()
    word_hash = getWordHash(today_date, HASH_KEY)
    day_word = getWordOfDay(game_words, word_hash)

    saveGameDetails(today_date, day_word, GAME_HISTORY_PATH)

    while game_attempts_counter < MAX_GAME_ATTEMPTS:

        today_date = date.today()
        word_hash_check = getWordHash(today_date, HASH_KEY)

        if word_hash_check != word_hash:
            clear()
            game_board = []
            game_attempts_counter = 0
            day_word = getWordOfDay(game_words, word_hash_check)
            print("La palabra ha cambiado, el juego se ha reiniciado.")
            continue
        
        if game_attempts_counter > 0:
            print()
        answer = askForWord("Ingresa una palabra: ")

        while " " in answer or not (answer.lower() in words) or len(answer) != WORDS_LENGTH:
            print(f"Error: Ingresa una palabra válida de {WORDS_LENGTH} letras sin espacios.")
            answer = askForWord("Intenta nuevamente: ")

        answer_chars = list(answer)
        clear()
        
        for i in range(len(day_word)):
            if answer_chars[i] == day_word[i]:
                answer_chars[i] = style_text(answer_chars[i], Back.GREEN, Fore.BLACK)
            elif answer_chars[i] in day_word:
                answer_chars[i] = style_text(answer_chars[i], Back.YELLOW, Fore.BLACK)
            else:
                answer_chars[i] = style_text(answer_chars[i], Back.WHITE, Fore.BLACK)

        game_board.append(answer_chars)
        print_colored_grid(game_board)

        if answer == day_word:
            print("\nGanaste.")
            break

        game_attempts_counter += 1

        if game_attempts_counter == MAX_GAME_ATTEMPTS:
            print("\nPerdiste.")

if __name__ == "__main__":
    main()