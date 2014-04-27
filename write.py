import sys, getopt, pickle
from markov.functions import create_matching
from markov import generator
from random import choice
DEBUG = False
text = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True
if len(sys.argv) == 2 and sys.argv[1] == "text":
    text = True

def main():
    if text:
        gen = generator.prose_generator()
        gen.read("corpus/shortpeterpan.txt")
        gen.perturb_tokens(.01)
        gen.create_ordered_paths()
    else:
        gen = generator.word_generator()
        gen.read("corpus/passwords.txt")
        gen.perturb_tokens(.01)
    gen.save("dictionaries/peterpan.pickle")
    sys.exit(0)

if __name__ == "__main__":
    main()
