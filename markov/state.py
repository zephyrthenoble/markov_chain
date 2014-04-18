class State:
    def __init__(self, length = 3):
        """creates the State, default length of 3"""
        self.state = [None for i in range(0, length)]
        self.length = length
        self.done = False
        self.constructed = ""
    def add(self, stritem):
        if stritem == "\n":
            self.done = True
        self.constructed += " " + stritem
        self.state.append(stritem)
        self.state.pop(0)
    def get(self, num):
        index = -1*num
        return " ".join(self.state[index:])
    def reset(self):
        self.state = [None for i in range(0, self.length)]
    def finished(self):
        return self.done
    def get_str(self):
        return self.constructed
    def __len__(self):
        count = 0
        for elem in self.state:
            if elem != None:
                count += 1
        return count
    def __str__(self):
        return "State: " + str(self.state) + " = " + self.constructed + "; " + str(self.finished())
