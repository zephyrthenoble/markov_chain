
import sys, getopt
from markov.functions import create_matching
from markov.generator import Generator
from random import choice

def main():
    #markov.read_from_folder("corpus")

    start = choice(single)
    constructed = start
    state = ["","",start]

    while state[-1] != '\n':
        one = state[-1]
        two = " ".join(state[-2]+state[-1]).strip()
        three = " ".join(state[-3]+state[-2]+state[-1]).strip()
        if one in ma1.keys():
            state.append(one)
            constructed += " " + ma1[one]
        elif two in ma2.keys():
            state.append(two)
            constructed += " " + ma2[two]
        elif three in ma3.keys():
            state.append(three)
            constructed += " " + ma3[three]
        else:
            print "Can't find", three
            break
    print start
    print state
    print constructed



if __name__ == "__main__":
    main()
