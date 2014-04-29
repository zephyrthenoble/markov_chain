import sys, getopt, pickle
from markov.functions import create_matching
from markov import generator
from random import choice
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
	DEBUG = True

def main():
	gen = generator.word_generator()
	gen.read("corpus/passwords.txt")
	gen.perturb_tokens(.01)
	gen.save("dictionaries/passwords.pickle")
	sys.exit(0)

if __name__ == "__main__":
	main()
