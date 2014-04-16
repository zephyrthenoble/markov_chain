from .functions import *
from collections import defaultdict
from random import random
import io



class Generator:
    def __init__(self):
        self.m = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

    def perturb_tokens(self, chance):
        num = (int)(len(self.m.keys()) * chance)
        for x in range(0,num):
            selected_key = choice(self.m.keys())
            test_token = selected_key.split()[-1]
            app_tokens = []
            for elem in self.m.keys():
                if elem.endswith(test_token) and elem != selected_key:
                    app_tokens.append(elem)
            if len(app_tokens) < 2:
                continue

            selected = self.m[selected_key]
            other = choice(self.m[choice(app_tokens)])
            print(selected_key + "+" + other)
            selected.append(other)

            

    def read_folder(self, folder):
        files = read_from_folder(folder)
        for elem in files:
            self.read(folder+'/'+elem)

    def read(self, filename):
        temp = []
        with open(filename) as f:
            temp = get_tokens(f.read())
            self.tokens.extend(temp)
        tst, tm = create_matching(temp)
        self.start_tokens.extend(tst)
        self.m.update(tm)
        self.start_tokens.extend(remove_duds(tst))
    
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
