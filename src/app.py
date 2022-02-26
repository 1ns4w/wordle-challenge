from datetime import datetime
from generator import getSpanishWords
from colorama import Back, Fore
from helpers import clear, normalize_words, print_colored_grid, style_text
from constants import GAME_ATTEMPTS, WORDS_LENGTH, TOTAL_WORDS, HASH_SUBSTRACTION

def main():

    clear()
    print(f"Cargando...")
    words = normalize_words(getSpanishWords(WORDS_LENGTH))
    game_words = words[:TOTAL_WORDS]

    game_grid = []
    attempts_counter = 0
    day_of_year = int(datetime.now().strftime('%j')) - HASH_SUBSTRACTION
    day_word = game_words[day_of_year - 1]
    clear()

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
            if answer_chars[i].strip() == day_word[i]:
                answer_chars[i] = style_text(Back.GREEN, Fore.BLACK, answer_chars[i])
            elif answer_chars[i].strip() in day_word:
                answer_chars[i] = style_text(Back.YELLOW, Fore.BLACK, answer_chars[i])
            else:
                answer_chars[i] = style_text(Back.WHITE, Fore.BLACK, answer_chars[i])

        game_grid.append(answer_chars)

        if answer == day_word:
            print("Ganaste.")
            break

        attempts_counter += 1

        if attempts_counter == GAME_ATTEMPTS:
            print("Perdiste.")

if __name__ == "__main__":
    main()