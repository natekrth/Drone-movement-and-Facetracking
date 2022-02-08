import re

def grep(string, filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().splitlines()
    for i in lines:
        if re.search(string, i):
            print(i)


grep('def', 'test')


