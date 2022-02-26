from colorama import Back, init, Style, Fore
import sys, platform, os
from datetime import datetime

def main():

    GAME_ATTEMPTS = 5
    INFILE_PATH = '../assets/palabras5.txt'

    infile = open(INFILE_PATH, 'r')
    words = lineBreakSeparatedValuesToArray(infile.read())
    normalized_words = normalize_words(words)

    attempts_counter = 0
    game_grid = []
    day_of_year = int(datetime.now().strftime('%j'))
    day_word = normalized_words[day_of_year - 1]
    print(day_word)

    while attempts_counter < GAME_ATTEMPTS:

        day_of_year_peek = int(datetime.now().strftime('%j'))

        if day_of_year_peek != day_of_year:
            game_grid = []
            attempts_counter = 0
            day_word = normalized_words[day_of_year_peek - 1]
            print("La palabra ha cambiado, es un nuevo día.")
            continue

        answer = input("Ingresa respuesta: ").strip()

        while not len(answer) == len(day_word):
            print(f"La respuesta debe tener una longitud de {len(day_word)}")
            answer = input("Ingresa respuesta nuevamente: ")

        answer_chars = list(answer)
        
        for i in range(len(day_word)):

            answer_chars[i] = f" {answer_chars[i]} "

            if answer_chars[i].strip() == day_word[i]:
                answer_chars[i] = Back.GREEN + Fore.BLACK + answer_chars[i]
            elif answer_chars[i].strip() in day_word:
                answer_chars[i] = Back.YELLOW + Fore.BLACK + answer_chars[i]
            else:
                answer_chars[i] = Back.WHITE + Fore.BLACK + answer_chars[i]

        game_grid.append(answer_chars)
        
        for row in game_grid:
            for letter in row:
                print(letter + Style.RESET_ALL, end=" ")
            print()

        if answer == day_word:
            print("¡Ganaste!")
            break

        attempts_counter += 1

        if attempts_counter == GAME_ATTEMPTS:
            print("Perdiste.")
        
    
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