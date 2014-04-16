import sys, getopt
from markov.functions import create_matching
from markov.generator import Generator
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    gen = Generator()
    gen.read_folder("corpus")
    print(gen.generate_sentences(4))
    maxkey = gen.m.keys()[0]
    maxvalue = gen.m[maxkey]
    for key, value in gen.m.items():
        if len(value) > 30:
                del key
                continue
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 2\n\n"
    print maxkey, sorted(maxvalue)


    st, ma = create_matching(gen.tokens, 1)
    maxkey = ma.keys()[0]
    maxvalue = [""]
    for key, value in ma.items():
        if len(value) > 30:
                del key
                continue
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 3\n\n"
    print maxkey, sorted(maxvalue)

    st, ma = create_matching(gen.tokens, 3)
    maxkey = ma.keys()[0]
    maxvalue = [""]
    for key, value in ma.items():
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 1\n\n"
    print maxkey, sorted(maxvalue)
    #markov.read_from_folder("corpus")


if __name__ == "__main__":
    main()
