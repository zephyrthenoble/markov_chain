class State:
    def __init__(self, length = 3):
        """creates the State, default length of 3"""
        self.state = [None for i in range(0, length)]
        self.length = length
        self.current_size = 0
        self.done = False
        self.constructed = ""
        self.min_size = 3
        self.max_size = 30
    def add(self, stritem):
        if stritem == "\n":
            if self.current_size >= self.min_size:
                self.done = True
            else:
                return
        self.current_size += 1
        if self.current_size >= self.max_size:
            self.done = True
        self.constructed += " " + stritem
        self.state.append(stritem)
        self.state.pop(0)
    def get(self, num):
        index = -1*num
        cons = ""
        for elem in self.state[index:]:
            if elem != None:
                cons+=" "+ elem
        cons = cons.strip()
        return cons
    def reset(self):
        self = State(length = self.length)
        self.constructed = ""
        self.state = [None for i in range(0, self.length)]
    def finished(self):
        return self.done
    def get_str(self):
        return self.constructed
    def get_word(self):
        return self.constructed.replace(" ", "")
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        elif self.state != other.state:
            return False
        elif str(self) != str(other):
            return False
        return True
    def __len__(self):
        count = 0
        for elem in self.state:
            if elem != None:
                count += 1
        return count
    def size(self):
        return self.current_size
    def __str__(self):
        return "State: " + str(self.state) + " = " + self.constructed + "; " + str(self.finished())
