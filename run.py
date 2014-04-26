
import sys, getopt, pickle, logging
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
from markov.state import State



def main():
    #load a generator
    gen = Generator.load("dictionaries/peterpan.pickle")
    #get a sentence
    print (gen.generate_sentence())

    count = 0
    val = gen.generate_sentence()
    #for x in range(0, 1000):
    #    print gen.generate_sentence()
    #sys.exit(0)
    while val != "julia":
        count+=1
        if count % 1000 == 0:
            print count
            print val
        val = gen.generate_sentence()
        #sys.stdout.write("\r%s %d" %(,count))

    print

    sys.exit(0)

if __name__ == "__main__":
    main()
