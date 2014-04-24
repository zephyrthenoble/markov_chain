from functions import *
from collections import defaultdict
import io, pickle, logging
from markov.state import State


class Generator:
    def __init__(self):
        self.m = defaultdict(list)
        self.ma1 = defaultdict(list)
        self.ma2 = defaultdict(list)
        self.ma3 = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

    @staticmethod
    def load(dest):
        return pickle.load(open(dest, "rb"))

    def save(self, dest):
        pickle.dump(self, open(dest, "wb"))

    def create_ordered_paths(self):
        """Run after adding all of the files to remove large and extra pathways"""
        #remove long single word probabilites
        print len(self.ma1.keys())
        for key, value in self.ma1.items():
            if len(value) > 15:
                self.ma1.pop(key, None)
                continue
        print len(self.ma1.keys())

        print
        #remove words that are in ma1, or are not of the right length
        print len(self.ma2.keys())
        maxcount = len(self.ma2.keys())/100
        count = 0
        for key, value in self.ma2.items():
            #this just prints out how much is done
            count += 1
            if count % maxcount == 0:
                sys.stdout.write ("\r%d%%" %(count / maxcount))
                sys.stdout.flush()
            flag = False
            #remove if in ma1
            for okey in self.ma1.keys():
                if key.split()[-1].strip() == okey:
                    self.ma2.pop(key, None)
                    flag = True
                    break
            if flag: continue
            #remove if too short or too long
            if len(value) > 15 or len(value) < 3:
                    self.ma2.pop(key, None)
                    continue
        print
        print len(self.ma2.keys())
            
        print
        print len(self.ma3.keys())
        #remove if key is in ma1 or ma2
        maxcount = len(self.ma3.keys())/100
        count = 0
        for key, value in self.ma3.items():
            count += 1
            if count % maxcount == 0:
                sys.stdout.write ("\r%d%%" %(count / maxcount))
                sys.stdout.flush()
            flag = False
            for okey in self.ma1.keys():
                if key.split()[-1].strip() == okey:
                    self.ma3.pop(key, None)
                    flag = True
                    break
            if flag: continue
            flag = False
            for okey in self.ma2.keys():
                #get the two words at the end of this 3 word key
                two_words = " ".join(key.split()[-2:]).strip()
                if two_words == okey:
                    self.ma3.pop(key, None)
                    flag = True
                    break
            if flag: continue
        print
        print len(self.ma3.keys())

    def read_folder(self, folder):
        files = read_from_folder(folder)
        for elem in files:
            self.read(folder+'/'+elem)
        self.create_ordered_paths()
    
    def read(self, filename):
        temp = []
        with open(filename) as f:
            temp = get_tokens(f.read())
            self.tokens.extend(temp)

        tst, tm = create_matching(temp, 1)
        self.m.update(tm)
        self.ma1.update(tm)

        tst, tm = create_matching(temp, 2)
        self.ma2.update(tm)

        tst, tm = create_matching(temp, 3)
        self.start_tokens.extend(remove_duds(tst))
        self.ma3.update(tm)
    
    def reset(self):
        self.m = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

    def generate_sentence(self):
        #print "generating"
        logging.basicConfig()

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.CRITICAL)

        ma1 = self.ma1
        ma2 = self.ma2
        ma3 = self.ma3
        triple = self.start_tokens 

        start = choice(triple)
        constructed = start
        state = State()
        for elem in start.split():
            state.add(elem.strip())

        one = state.get(1)
        two = state.get(2)
        three = state.get(3)

        logger.debug("logger.debuging dictionaries\n")
        logger.debug("\nma1")
        for key, val in list(ma1.items()):
            logger.debug(key +" "+str(val))

        logger.debug("\nma2")
        for key, val in list(ma2.items()):
            logger.debug(key +" "+str(val))

        logger.debug("\nma3")
        for key, val in list(ma3.items()):
            logger.debug(key +" "+str(val))
        logger.debug("=======================\nlogger.debuging start and state")

        logger.debug(start)
        logger.debug(state)



        while state.finished() == False:
            word = ""
            one = state.get(1)
            two = state.get(2)
            three = state.get(3)
            logger.debug("Current state:")
            logger.debug(state)

            if one in list(ma1.keys()):
                logger.debug("Found in 1")
                word = choice(ma1[one])
            elif two in list(ma2.keys()):
                logger.debug("Found in 2")
                word = choice(ma2[two])
            elif three in list(ma3.keys()):
                logger.debug("Found in 3")
                word = choice(ma3[three])
            else:
                # not exactly in a key
                # change this to adding to a list and choice from it
                logger.debug("Searching for "+ one)
                possible = []
                flag = True
                for key, values in list(ma2.items()):
                    logger.debug("key  "+key+" in 2")
                    if key.endswith(one):
                        logger.debug("Found one in 2 keys (end)")
                        logger.debug(key)
                        c = choice(values)
                        if c not in possible:
                            possible.append(c)
                    elif key.startswith(one):
                        logger.debug("Found one in 2 keys (start)")
                        logger.debug(key)
                        c = key.split()[1].strip()
                        if c not in possible:
                            possible.append(c)

                for key, values in list(ma3.items()):
                    logger.debug("key  "+key+" in 3")
                    if key.endswith(one):
                        logger.debug("Found one in 3 keys (end)")
                        logger.debug(key)
                        c = choice(values)
                        if c not in possible:
                            possible.append(c)
                    elif key.startswith(one):
                        logger.debug("Found one in 3 keys (start)")
                        logger.debug(key)
                        c = key.split()[1].strip()
                        if c not in possible:
                            possible.append(c)
                    elif key.split()[1].strip() == one:
                        logger.debug("Found one in 3 keys (middle)")
                        logger.debug(key)
                        c = key.split()[2].strip()
                        if c not in possible:
                            possible.append(c)
                if len(possible) == 0:
                    logger.debug("Can't find " + three)
                    break

                logger.debug("possible")
                logger.debug(possible)
                word = choice(possible)

            logger.debug("Word is "+ word)
            state.add(word)
        logger.info(start)
        logger.info(state.get_str())

        constructed = state.get_str().strip() + "." #construct_sentences(self.start_tokens, self.m)
        self.prev.append(constructed)
        return constructed

    def generate_sentences(self, count):
        sentences = ""
        for x in range(0, count):
            sentences = sentences + "  "+self.generate_sentence()
        return sentences
