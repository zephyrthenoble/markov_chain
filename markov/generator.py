from functions import *
from collections import defaultdict


class Generator:
    def __init__(self):
        self.m = defaultdict(list)
        self.tokens = []
        self.start_tokens = []
        self.prev = []

