import re
import os

try:
    while True:
        lang = {}
        lang[1] = ["American English", "/usr/share/dict/american-english"]
        lang[2] = ["British English", "/usr/share/dict/british-english"]
        lang[3] = ["Spanish", "/usr/share/dict/spanish"]
        lang[4] = ["Italian", "/usr/share/dict/italian"]
        lang[5] = ["Catalan", "/usr/share/dict/catala"]
        lang[6] = ["French", "/usr/share/dict/french"]
        lang[7] = ["German", "/usr/share/dict/german"]
        lang[8] = ["Finnish", "/usr/share/dict/finnish"]

        for key in lang:
            print(f"{key}) {lang[key][0]}")

        dict = input("Select a Dictionary [1-8]: ")
        while not re.search(r'^[1-8]$', dict):
            dict = input("Select a Dictionary [1-8]: ")

        dict = int(dict)
        words = open(lang[dict][1], 'r').read().lower()

        letters = input("Enter your letters with no spaces: ")
        occurences = {}

        for letter in letters:
            occurences[letter] = occurences[letter] + \
                1 if letter in occurences else 1

        regex = r'\b[' + letters + ']{1,' + str(len(letters)) + '}\\b'

        matches = set(re.findall(regex, words))
        entries = set(matches)
        for match in matches:
            for letter in match:
                if len(re.findall(letter, match)) > occurences[letter]:
                    entries.remove(match)
                    break

        output = sorted(entries, key=lambda x: (len(x), x))

        length = 0
        for entry in output:
            if len(entry) > length:
                length = len(entry)
                print("-----------------")
                print(f"{length} letter words: ")
                print("-----------------")
            print(entry)
        if input("\nContinue? (Y/n) ").lower() == 'n':
            break
        else:
            os.system('clear')
except KeyboardInterrupt:
    print("Exiting...")
except EOFError:
    print("Exiting...")
