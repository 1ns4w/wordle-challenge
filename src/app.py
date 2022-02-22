from colorama import Fore
from requests_html import HTMLSession

def get5LengthWords():
    session = HTMLSession()
    page = session.get("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
    print(page.status_code )

def normalizeVowel(vowel):
    vowels = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    if vowel.lower() not in vowels:
        return vowel
    return vowels[vowel.lower()].upper() if vowel.isupper() else vowels[vowel]

print(normalizeVowel('á'))

word = 'REINA'

print(get5LengthWords())