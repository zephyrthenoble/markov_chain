import random, time
from collections import defaultdict

rands = defaultdict(int)
for x in range(0, 100000):
    rands[x]=random.random()

total = []
tests = 1000
for x in range(0, tests):
    search = random.randrange(len(rands.keys()))
    t0 = time.time()
    if search in rands.keys():
        word = rands[search]
        pass
    t1 = time.time()

    total.append(t1-t0)

length = len(total)
sum = 0
for elem in total:
    sum += elem
print sum/length

for x in range(0, tests):
    search = random.randrange(len(rands.keys()))
    t0 = time.time()
    for key, value in rands.items():
        if key == search:
            word = value
            break
    t1 = time.time()

    total.append(t1-t0)

length = len(total)
sum = 0
for elem in total:
    sum += elem
print sum/length

