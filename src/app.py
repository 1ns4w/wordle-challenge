def normalizeVowel(vowel):
    vowels = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    if vowel.lower() not in vowels:
        return vowel
    return vowels[vowel.lower()].upper() if vowel.isupper() else vowels[vowel]

print(normalizeVowel('á'))

word = 'REINA'