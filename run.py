
import sys, getopt, json
from markov.functions import create_matching
from markov.generator import Generator
from random import choice

def main():
    #markov.read_from_folder("corpus")
    ma1 = json.load(open("dictionaries/ma1.json"))
    ma2 = json.load(open("dictionaries/ma2.json"))
    ma3 = json.load(open("dictionaries/ma3.json"))
    single = json.load(open("dictionaries/single.json"))

    start = choice(single)
    constructed = start
    state = ["","",start]
    print start
    print constructed
    print state
    print

    while state[-1] != '\n':
        word = ""
        one = state[-1]
        two = " ".join(state[-2]+state[-1]).strip()
        three = " ".join(state[-3]+state[-2]+state[-1]).strip()
        print constructed
        print state
        print

        if two == one:
            flag = True
            for elem in ma2.keys():
                if elem.endswith(one):
                    word = choice(ma2[elem])
                    break
        if three == two:
            flag = True
            for elem in ma3.keys():
                if elem.endswith(two):
                    word = choice(choice(ma3[elem]))
                    break
        if flag == False:
            if one in ma1.keys():
                word = choice(ma1[one])
            elif two in ma2.keys():
                word = choice(ma2[two])
            elif three in ma3.keys():
                word = choice(ma3[three])
            else:
                print "Can't find", three
                break
        state.append(word)
        constructed += " " + word
    print start
    print state
    print constructed



if __name__ == "__main__":
    main()
