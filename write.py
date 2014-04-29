import sys, getopt, pickle
from markov.functions import create_matching
from markov import generator
from random import choice
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
	text = raw_input("Enter text: ")
	if text == "":
		text = "shortpeterpan.txt"

    	gen = generator.prose_generator()
    	gen.read("corpus/" + text)
    	gen.perturb_tokens(.01)
    	gen.create_ordered_paths()
	gen.save("dictionaries/" + text[:-4] + ".pickle")
    	sys.exit(0)

if __name__ == "__main__":
    main()
