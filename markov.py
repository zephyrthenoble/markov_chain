"""markov.py"""
from random import choice, randrange
from collections import defaultdict 
from pprint import pprint
import sys
read_file = "testfinn.txt"
DEBUG = True


def process_string(string):
    space = ['\n','\r']
    unwanted = ['_']
    for elem in space:
        string = string.replace(elem, ' ')
    for elem in unwanted:
        string = string.replace(elem, '')
    return string.strip()
if DEBUG:
    def prt(to_print):
        print to_print
else:
    def prt(to_print):
        pass
def get_tokens(complete_file):
    #starting sentence
    builder = ""
    ##completed sentences
    sentences = []
    #go through each character
    check = False
    sp = False
    for c in complete_file:
        #add it
        builder = builder + c
        #if it is a quote, handle options
        if c == '"':
            #if it was preceded by a checked sentence-ender, end sentence
            if sp:
                sentences.append(process_string(builder))
                builder = ""
            #if it wasn't, it's part of an internal quote, continue
            if check:
                check = False
            #if it was the first quote, check for the end quote before finishing
            else:
                check = True
        #if we expected a quote to end the quoted sentence, but there isn't one
        #we have the end of a sentence contained in the quote, continue
        else:
            if sp:
                sp = False
        #sentence enders
        if c == '.' or c == '?' or c == '!':
            #if inside a quote, check for end quote
            if check:
                sp = True
            # otherwise you have a sentence
            else:
                if len(builder) < 5 or builder.endswith("Mr.") or builder.endswith("Mrs.") or builder.endswith("Ms.") or builder.endswith(" ."):
                    continue
                sentences.append(process_string(builder))
                builder = ""
    builder = process_string(builder)
    if builder !="":
        sentences.append(builder)
    return sentences


tokens = []
with open(read_file, 'r') as f:
    text = f.read()
    tokens = get_tokens(text)
pprint(tokens)
sys.exit(0)
m = defaultdict(list)
for token in tokens:
    t = token .split()
    if len(t) < 2: continue
    first = t[0]
    second = t[1]
    for index in range(2, len(t)):
        word = t[index]
        while word.endswith('.') or word.endswith('?') or word.endswith('!'):
            if len(word) < 2:
                break
            print word
            word = word[-1].strip()
        m[first +" "+ second].append(word)
        #prt(first+second+" "+token[index])
        first = second
        second = t[index]
    m[first + " " + second].append('\n')

for key, value in sorted(m.items()):
    print key, sorted(value)
    pass


sys.exit(0)

m = defaultdict(list)
for token in tokens:
    if len(token) > 1:
        first = token[0]
        second = token[1]
        for index in range(2, len(token)):
            m[first + second].append(token[index])
            #prt(first+second+" "+token[index])
            first = second
            second = token[index]
        m[first + second].append('\0')

for key, value in sorted(m.items()):
    print key, sorted(value)
    pass


print 

for x in range (0, 4):
    seed = choice(m.keys())
    output = seed
    while "\0" not in output and len(output) < 30:
        output= output + choice(m[seed])
    print output

