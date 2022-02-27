from os import system
from colorama import Style

def style_text(word, back, fore):
    return back + fore + f" {word} " + Style.RESET_ALL

def clear():
    system("clear||cls")

def print_colored_grid(grid):
    for i in range(len(grid)):
        if i > 0:
            print("\n")
        for j in range(len(grid[i])):
            print(grid[i][j], end = "  ")
    print()

def normalize_words(words):
    accents_equivalents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for i in range(len(words)):
        for accent in accents_equivalents.keys():
            words[i] = words[i].replace(accent, accents_equivalents[accent])
    return words

def lineBreakSeparatedValuesToArray(text):
    return text.split("\n")[:-1] if text.split("\n")[-1] == '\n' else text.split("\n")