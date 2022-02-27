from os import path, stat
from datetime import datetime
from colorama import Back, Fore, init
from generator import getSpanishWords
from constants import GAME_ATTEMPTS, WORDS_LENGTH, TOTAL_WORDS, HASH_SUBSTRACTION, INFILE_PATH
from helpers import clear, normalize_words, print_colored_grid, style_text, lineBreakSeparatedValuesToArray

def main():

    init()
    clear()

    if path.exists(INFILE_PATH) == False or stat(INFILE_PATH).st_size == 0:
        print(f"Cargando...")
        words = normalize_words(getSpanishWords(WORDS_LENGTH))
    else:
        infile_text = open(INFILE_PATH, 'r').read()
        words = normalize_words(lineBreakSeparatedValuesToArray(infile_text))

    clear()

    game_words = words[:TOTAL_WORDS]
    game_grid = []
    attempts_counter = 0

    day_of_year = int(datetime.now().strftime('%j')) - HASH_SUBSTRACTION
    day_word = game_words[day_of_year - 1]

    while attempts_counter < GAME_ATTEMPTS:

        day_of_year_peek = int(datetime.now().strftime('%j')) - HASH_SUBSTRACTION

        if day_of_year_peek != day_of_year:
            game_grid = []
            attempts_counter = 0
            day_word = game_words[day_of_year_peek - 1]
            clear()
            print("La palabra ha cambiado, es un nuevo día.")
            continue
        
        answer = input("Ingresa una palabra: ")

        while " " in answer or not (answer in words) or len(answer) != WORDS_LENGTH:
            print(f"Error: Ingresa una palabra válida de {WORDS_LENGTH} letras sin espacios.")
            answer = input("Intenta nuevamente: ")

        answer_chars = list(answer)
        clear()
        
        for i in range(len(day_word)):
            if answer_chars[i] == day_word[i]:
                answer_chars[i] = style_text(answer_chars[i], Back.GREEN, Fore.BLACK)
            elif answer_chars[i] in day_word:
                answer_chars[i] = style_text(answer_chars[i], Back.YELLOW, Fore.BLACK)
            else:
                answer_chars[i] = style_text(answer_chars[i], Back.WHITE, Fore.BLACK)

        game_grid.append(answer_chars)
        print_colored_grid(game_grid)

        if answer == day_word:
            print("Ganaste.")
            break

        attempts_counter += 1

        if attempts_counter == GAME_ATTEMPTS:
            print("Perdiste.")

if __name__ == "__main__":
    main()