import os
import glob
import re

encoding = "ISO-8859-1"

def main():
    needToSortAndRemoveDuplicates = False
    with open("../FULL.txt", "a", encoding=encoding) as FULL:
        for folder in os.listdir('../Wordlists'):
            isWordlist = os.fsdecode(folder).endswith('.wordlist')
            isNew = not os.path.isfile(f'../Wordlists/{folder}/.imported')
            if isWordlist and isNew:
                if not needToSortAndRemoveDuplicates:
                    print('Importing...')
                needToSortAndRemoveDuplicates = True
                print('  +  ' + os.fsdecode(folder))
                for file in os.listdir(f'../Wordlists/{folder}'):
                    with open(f'../Wordlists/{folder}/{file}', "r", encoding=encoding) as f:
                            FULL.write(f.read())

                dotImported = open(f'../Wordlists/{folder}/.imported',"w+", encoding=encoding)
        FULL.close()

    if needToSortAndRemoveDuplicates:
        print('Done importing.\n\nUse sort-remove.sh now.')
        # with open("../FULL.txt", "r", encoding=encoding) as FULL:
        #     bigList = sorted(list(set(re.split('\n', FULL.read()))))
        # with open("../FULL.txt", "w") as FULL:
        #     FULL.write(''.join(line + '\n' for line in bigList))
        #     FULL.close()
        # print('Finished sort and uniqueing.')
    else:
        print('Nothing new to import.')

if __name__ == '__main__':
    main()
