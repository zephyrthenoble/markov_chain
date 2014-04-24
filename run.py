
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
    sys.exit(0)

if __name__ == "__main__":
    main()
