from colorama import Fore
import sys, platform, os
from words import getSpanishWords

def main():

    getSpanishWords(5, "palabras5.txt")
    sys.exit(0)

if __name__ == "__main__":
    main()

"""
if len(sys.argv) != 2:
    message = "Usage: python app.py <words length>"
    if platform.system() != "Windows":
        print(message.replace("python", "python3"))
    else:
        print(message)
    sys.exit(1)

words_length = sys.argv[1]
"""