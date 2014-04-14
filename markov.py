"""markov.py"""
from random import choice, randrange
from collections import defaultdict 
from pprint import pprint
import sys, getopt
read_file = "input.txt"
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

if DEBUG:
    def prt(to_print):
        print(to_print)
else:
    def prt(to_print):
        pass

def check_periods(builder):
    check = ["Mr.","Mrs.", "Ms.", " .", "No."]

    for elem in check:
        if builder.endswith(elem):
            return True
    return False

def process_string(string):
    space = ['\n','\r', '--']
    unwanted = ['_','"','[',']']
    for elem in space:
        string = string.replace(elem, ' ')
    for elem in unwanted:
        string = string.replace(elem, '')
    return string[:-1].strip()
def get_tokens(complete_file):
    #starting sentence
    builder = ""
    ##completed sentences
    sentences = []
    #go through each character
    check = False
    internal_quote = False
    sp = False
    index = 0
    for c in complete_file:
        index += 1
        #add it
        builder = builder + c
        #if it is a quote, handle options
        if c == '"':
            #if it was preceded by a checked sentence-ender, end sentence
            if sp:
                #check if it was at then end of a quote or not
                #print "checking"
                endindex = index+20
                if index+20 > len(complete_file):
                    endindex = len(complete_file)
                #print endindex
                temp = complete_file[index+1:endindex]
                #print temp
                next_word = temp.strip().split()[0]
                #print next_word
                if next_word != next_word.lower():
                    #print "appended"
                    sp = False
                    sentences.append(process_string(builder))
                    builder = ""
            #if it wasn't, it's part of an internal quote, continue
            if check:
                check = False
            #if it was the first quote, check for the end quote before finishing
            else:
                check = True
        #else if c =="'":
        #    if check:
        #        if internal_quote:
        #            internal_quote = False
        #        else:
        #            internal_quote = True
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
                if len(builder) < 5 or check_periods(builder):
                    continue
                sentences.append(process_string(builder))
                builder = ""
    builder = process_string(builder)
    if builder !="": # and builder != '!' and builder != '.' and builder != '?':
        sentences.append(builder)
    return sentences

#get tokens
tokens = []
with open(read_file, 'r') as f:
    text = f.read()
    tokens = get_tokens(text)

#pprint(tokens)
#sys.exit(0)

#things that start a sentence, which hopefully gives us better results
start_tokens = []
#the dictionary that will contain the tokens and their options
m = defaultdict(list)
for token in tokens:
    t = token.split()
    if len(t) < 2: continue
    #get the first and second words, to create a better matching
    first = t[0]
    second = t[1]
    start_tokens.append(first+' '+second)
    for index in range(2, len(t)):
        word = t[index]
        while word.endswith('.') or word.endswith('?') or word.endswith('!'):
            if len(word) < 2:
                break
            #prt(word)
            word = word[:-1].strip()
        m[first +" "+ second].append(word)
        #prt(first+second+" "+token[index])
        first = second
        second = t[index]
    m[first + " " + second].append('\n')

if DEBUG:
    for key, value in sorted(m.items()):
        print(key, sorted(value))
        pass

#sys.exit(0)
temp = m

x = 0
constructed = choice(start_tokens)
first, second = constructed.split()
while '\n' not in constructed and len(constructed) < 200:
    if len(temp[first + ' ' + second]) <=0:
        break
    nextvalue = choice(temp[first+' '+second])
    del temp[first+' '+second]
    if nextvalue.strip() == '.' or nextvalue.strip() == '?' or nextvalue.strip() == '!':
        continue
    constructed = constructed + ' ' + nextvalue
    first = second
    second = nextvalue

constructed = constructed.replace('\n','').strip()+'.'
print(constructed)

