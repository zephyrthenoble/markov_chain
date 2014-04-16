import sys, getopt
from markov.generator import Generator
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    gen = Generator()
    gen.read_folder("corpus")
    #gen.perturb_tokens(0.03)
    print(gen.generate_sentences(4))
    #markov.read_from_folder("corpus")


if __name__ == "__main__":
    main()
