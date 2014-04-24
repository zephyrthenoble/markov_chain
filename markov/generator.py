from functions import *
from collections import defaultdict
import io


class Generator:
    def __init__(self):
        self.m = defaultdict(list)
        self.ma1 = defaultdict(list)
        self.ma2 = defaultdict(list)
        self.ma3 = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

    def read_folder(self, folder):
        files = read_from_folder(folder)
        for elem in files:
            self.read(folder+'/'+elem)

    def read(self, filename):
        temp = []
        with open(filename) as f:
            temp = get_tokens(f.read())
            self.tokens.extend(temp)

        tst, tm = create_matching(temp, 1)
        self.start_tokens.extend(remove_duds(tst))
        self.m.update(tm)
        self.ma1.update(tm)

        tst, tm = create_matching(temp, 2)
        self.ma2.update(tm)

        tst, tm = create_matching(temp, 3)
        self.ma3.update(tm)
    
    def reset(self):
        self.m = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

    def generate_sentence(self):
        constructed = construct_sentences(self.start_tokens, self.m)
        self.prev.append(constructed)
        return constructed

    def generate_sentences(self, count):
        sentences = ""
        for x in range(0, count):
            sentences = sentences + "  "+self.generate_sentence()
        return sentences
