import sys, getopt
from markov.generator import Generator
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    gen = Generator()
    gen.read_folder("corpus")
    print(gen.generate_sentences(4))
    #markov.read_from_folder("corpus")


if __name__ == "__main__":
    main()
