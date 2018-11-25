import json
from os import listdir
from os.path import isfile, join
if __name__ == '__main__':
    mypath = 'etc/items/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    verbs = ['talk',
             'eat',
             'look at/view',
             'move',
             'climb',
             'feed',
             'hit',
             'lift',
             'take',
             'use']
    for file in onlyfiles:
        with open(mypath + file, 'r') as f:
            d = json.load(f)
        item_name = file.replace('.json', '')
        print(item_name)
        print(d)
