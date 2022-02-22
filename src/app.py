from colorama import Fore
import sys, platform, os
from generator import getSpanishWords
from datetime import datetime

def main():

    infile_path = input("File with words path: ")

    if os.path.exists(infile_path) == False or os.stat(infile_path).st_size == 0:
        getSpanishWords(5, infile_path, 20)
    
    infile = open(infile_path, 'r')
    print(infile.read())

if __name__ == "__main__":
    main()