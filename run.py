#! /usr/bin/env python
import sys, getopt, pickle, logging, time, multiprocessing, copy, signal
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
from markov.state import State

def signal_handler(signal, frame):
	print("You pressed Ctrl+C")
	for elem in processes:
		elem.terminate()
		elem.join()
	sys.exit(0)

processes = []
test = "julia"
if len(sys.argv) == 2:
    test = sys.argv[1]


def main():
    signal.signal(signal.SIGINT, signal_handler)
    #load a generator
    dic = raw_input("Enter your dictionary: ")
    if dic == "":
	    dic = "shortpeterpan.pickle"
    gen = Generator.load("dictionaries/" + dic)
    #get a sentence
    print "A test output"
    print (gen.generate_sentence())

    count = 0
    sentences = []
    if gen.text:
        for x in xrange(1000):
            sentences.append(gen.generate_sentence())
        for elem in sorted(sentences):
            print elem
    else:
        gen.min_size = len(test)
        gen.max_size = len(test)
        val = gen.generate_word()
        maxcount = 26**len(test)
        count_index = maxcount / 100


        tlist = []
        plist = []
        print "Looking for", test,"out of", maxcount, "combinations (26^"+str(len(test))+")"
        cores = multiprocessing.cpu_count()
        tests = 10
        print "Cores", cores
        if cores <=1:
            cores = 2

        for x in xrange(tests):
            count = 0
            print "Test",x
            q = multiprocessing.Queue()
            processes = []
            count = 0
            for x in xrange(cores - 1):
                p = multiprocessing.Process(target = run, args=(gen, q))
                processes.append(p)
            for elem in processes:
                elem.start()

            t0 = time.time()
            while q.get() != test:
                count+=1
                if count % (count_index/100) == 0:
                    sys.stdout.write("\r%f%%" %((float)(count)/(float)(maxcount)))
                    sys.stdout.flush()
            t1 = time.time()
            tlist.append(t1-t0)
            plist.append((float)(count)/(float)(maxcount))
            for elem in processes:
                elem.terminate()
            print
            print count
        print "Average time:\t\t\t", sum(tlist)/len(tlist)
        print "Average percent searched:\t", sum(plist)/len(tlist)



    sys.exit(0)

def old():

        #with open("output/"+test+".txt", "w") as f:
            t0 = time.time()
            val = gen.generate_word()
            while val != test:
                count+=1
                #print count
                if count % (count_index/100) == 0:
                    #sys.stdout.write("\r%f%%" %((float)(count)/(float)(count_index)))
                    sys.stdout.write("\r%f%%" %((float)(count)/(float)(maxcount)))
                    sys.stdout.flush()
                  #  print val
                val = gen.generate_word()
                #sentences.append(val)
                #if len(sentences) >= 1024:
                #    f.write("\n".join(sentences))
                #    sentences = []
            t1 = time.time()
            tlist.append(t1-t0)
            plist.append((float)(count)/(float)(maxcount))
            print
            print count
        #print "Average time:\t\t\t", sum(tlist)/len(tlist)
        #print "Average percent searched:\t", sum(plist)/len(tlist)
def run(gen, q):
    while True:
        q.put(gen.generate_word())

if __name__ == "__main__":
    main()
