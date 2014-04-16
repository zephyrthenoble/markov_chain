
import sys, getopt, json
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
DEBUG = False

if len(sys.argv) == 2 and sys.argv[1] == "debug":
    DEBUG = True

def main():
    gen = Generator()
    gen.read_folder("corpus")
    print(gen.generate_sentences(4))

    json.dump(gen.m, open("dictionaries/m.json", "w"))


    single, ma1 = create_matching(gen.tokens, 1)
    json.dump(single, open("dictionaries/single.json", "w"))

    maxkey = ma1.keys()[0]
    maxvalue = [""]
    for key, value in ma1.items():
        if len(value) > 15 or len(value) < 3:
            ma1.pop(key, None)
            continue
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 3\n\n"
    print maxkey, sorted(maxvalue)
    print len(ma1.keys())

    ma2 = gen.m
    maxkey = ma2.keys()[0]
    maxvalue = ma2[maxkey]

    maxcount = len(ma2.keys())/100
    count = 0
    print
    for key, value in ma2.items():
        count += 1
        if count % maxcount == 0:
            sys.stdout.write ("\r%d%%" %(count / maxcount))
            sys.stdout.flush()
        flag = False
        for okey in ma1.keys():
            if key.split()[-1].strip() == okey:
                ma2.pop(key, None)
                flag = True
                break
        if flag: continue
        if len(value) > 15 or len(value) < 3:
                ma2.pop(key, None)
                continue
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 2\n\n"
    print maxkey, sorted(maxvalue)
    print len(ma2.keys())
    #for key, value in ma2.items():
    #    print key, value

    st, ma3 = create_matching(gen.tokens, 3)
    maxkey = ma3.keys()[0]
    maxvalue = [""]
    maxcount = len(ma3.keys())/100
    count = 0
    for key, value in ma3.items():
        count += 1
        if count % maxcount == 0:
            sys.stdout.write ("\r%d%%" %(count / maxcount))
            sys.stdout.flush()
        flag = False
        for okey in ma1.keys():
            if key.split()[-1].strip() == okey:
                ma3.pop(key, None)
                flag = True
                break
        if flag: continue
        flag = False
        for okey in ma2.keys():
            if key.split()[-1].strip() == okey:
                ma3.pop(key, None)
                flag = True
                break
        if flag: continue
        if len(value) > len(maxvalue):
            maxvalue = value
            maxkey = key
    print "=================\nMax for 1\n\n"
    print maxkey, sorted(maxvalue)
    print len(ma3.keys())


    json.dump(ma1, open("dictionaries/ma1.json", "w"))
    json.dump(ma2, open("dictionaries/ma2.json", "w"))
    json.dump(ma3, open("dictionaries/ma3.json", "w"))



if __name__ == "__main__":
    main()
