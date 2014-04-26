"""markov.py"""
from random import choice, randrange
from collections import defaultdict 
from pprint import pprint
from os import walk
import sys, getopt
read_file = "peterpan.txt"
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

if DEBUG:
    def prt(to_print):
        print(to_print)
else:
    def prt(to_print):
        pass

def read_from_folder(dirname):
    files = []
    for (dirpath, dirnames, filenames) in walk(dirname):
        files.extend(filenames)
    return files

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

def remove_duds(start_tokens):
    for elem in start_tokens:
        #remove elements that don't start with a capital letter
        if elem[0] == elem[0].lower():
            #prt(sorted(elem))
            if elem[0] == "'" and len(elem) > 1:
                if elem[1] != elem[1].lower():
                    continue
            del elem
    return start_tokens

def create_matching(tokens, count):
    #things that start a sentence, which hopefully gives us better results
    start_tokens = []
    #the dictionary that will contain the tokens and their options
    m = defaultdict(list)

    for token in tokens:
        t = token.split()
        if len(t) == 1:
            t = list(t[0])
        print t
        if len(t) < count: continue
        #get the first and second words, to create a better matching
        state = [t[i] for i in range(0,count)]
        #first = t[0]
        #second = t[1]
        constructed = ""
        for elem in state:
            constructed += elem + " "
        #start_tokens.append(first+' '+second)
        start_tokens.append(constructed.strip())
        for index in range(count, len(t)):
            word = t[index]
            while word.endswith('.') or word.endswith('?') or word.endswith('!'):
                if len(word) < count:
                    break
                #prt(word)
                word = word[:-1].strip()
            constructed = ""
            for elem in state:
                constructed += elem + " "
            m[constructed.strip()].append(word)
            #prt(first+second+" "+token[index])
            for i in range(0, len(state)-1):
                state[i] = state[i+1]
            state[-1] = word
            #first = second
            #second = t[index]
        constructed = ""
        for elem in state:
            constructed += elem + " "
        m[constructed.strip()].append('\n')

    return (start_tokens, m)

def construct_sentences(start_tokens, m):
    #later, if we want to do this multiple times, we can just keep setting temp to m
    temp = m
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
    return constructed

def read_tokens(read_file):
    tokens = []
    with open(read_file, 'r') as f:
        text = f.read()
        tokens = get_tokens(text)
    return tokens

def main():
    tokens = read_tokens(read_file)
    start_tokens, m = create_matching(tokens)
    if DEBUG:
        for key, value in sorted(m.items()):
            print(key, sorted(value))
            pass

    prt("Removing dud starting elements")
    #remove dud starting tokens
    start_tokens = remove_duds(start_tokens)

    x = 0
    constructed = construct_sentences(start_tokens, m)

    print(constructed)

if __name__ == "__main__":
    main()
