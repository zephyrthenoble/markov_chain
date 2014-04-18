
import sys, getopt, pickle, logging
from markov.functions import create_matching
from markov.generator import Generator
from random import choice
from markov.state import State



def main():
    logging.basicConfig()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    ma1 = pickle.load(open("dictionaries/ma1.pickle", "rb"))
    ma2 = pickle.load(open("dictionaries/ma2.pickle", "rb"))
    ma3 = pickle.load(open("dictionaries/ma3.pickle", "rb"))
    triple = pickle.load(open("dictionaries/triple.pickle", "rb"))

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

    sys.exit(0)


if __name__ == "__main__":
    main()
