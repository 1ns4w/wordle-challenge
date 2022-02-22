from colorama import Fore
import requests

def getSomeLengthWords(lenght):
    page = requests.get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    page_content = page.text
    print(page_content)

def normalizeVowel(vowel):
    vowels = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    if vowel.lower() not in vowels:
        return vowel
    return vowels[vowel.lower()].upper() if vowel.isupper() else vowels[vowel]

print(normalizeVowel('á'))

word = 'REINA'

print(getSomeLengthWords(2))