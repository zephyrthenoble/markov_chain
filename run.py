import sys, getopt
from markov import generator
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    print
    #markov.read_from_folder("corpus")


if __name__ == "__main__":
    main()