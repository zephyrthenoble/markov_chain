
import sys, getopt, pickle, logging
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
from markov.state import State


test = "julia"
if len(sys.argv) == 2:
    test = sys.argv[1]


def main():
    #load a generator
    gen = Generator.load("dictionaries/peterpan.pickle")
    #get a sentence
    print "A test output"
    print (gen.generate_sentence())

    count = 0
    sentences = []
    if gen.text:
        for x in range(0, 1000):
            sentences.append(gen.generate_sentence())
        for elem in sorted(sentences):
            print elem
    else:
        gen.min_size = len(test)
        gen.max_size = len(test)
        val = gen.generate_word()
        maxcount = 26**len(test)
        count_index = maxcount / 100
        print test, maxcount, count_index, count_index/100
        with open("output/"+test+".txt", "w") as f:
            while val != test:
                count+=1
                #print count
                if count % (count_index/100) == 0:
                    sys.stdout.write("\r%f%%" %((float)(count)/(float)(count_index)))
                    sys.stdout.flush()
                  #  print val
                val = gen.generate_word()
                #sentences.append(val)
                #if len(sentences) >= 1024:
                #    f.write("\n".join(sentences))
                #    sentences = []

        print
        print count


    sys.exit(0)

if __name__ == "__main__":
    main()
