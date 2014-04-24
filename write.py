
import sys, getopt, pickle
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    gen = Generator()
    #gen.read_folder("corpus")
    #gen.read("corpus/shortpeterpan.txt")
    gen.read("corpus/peterpan.txt")
    gen.perturb_tokens(.01)
    gen.create_ordered_paths()
    gen.save("dictionaries/peterpan.pickle")
    sys.exit(0)

if __name__ == "__main__":
    main()
