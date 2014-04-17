
import sys, getopt, pickle
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
from markov.state import State




def main():
    ma1 = pickle.load(open("dictionaries/ma1.pickle", "rb"))
    ma2 = pickle.load(open("dictionaries/ma2.pickle", "rb"))
    ma3 = pickle.load(open("dictionaries/ma3.pickle", "rb"))
    triple = pickle.load(open("dictionaries/triple.pickle", "rb"))


#     print "ma1"
#     for key, val in ma1.items():
#         print key, val
# 
#     print
#     print "ma2"
#     for key, val in ma2.items():
#         print key, val
# 
#     print
#     print "ma3"
#     for key, val in ma3.items():
#         print key, val
# 
    start = choice(triple)
    constructed = start
    state = State()
    for elem in start.split():
        state.add(elem.strip())
    print start
    print constructed
    print state




    sys.exit(0)

    while !(state.finished):
        word = ""
        one = state.get(1)
        two = state.get(2)
        three = state.get(3)
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
        state.pop(0)
        constructed += " " + word
    print start
    print state
    print constructed



if __name__ == "__main__":
    main()
