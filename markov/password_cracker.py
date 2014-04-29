import sys, multiprocessing, time, signal

def signal_handler(signal, frame):
    print("You pressed Ctrl+C")
    for elem in processes:
        elem.terminate()
    for elem in processes:
        while elem.is_alive():
            elem.terminate()
    sys.exit(0)

processes = []

def run(gen, q):
    while True:
        q.put(gen.generate_word())

def create_tree(depth, gen):
    tree = Node("")

    for elem in set(gen.ma1.keys()):
        node = create_tree_helper(depth-1, elem, gen.ma1)
        tree.add(1, node)
        

class Node:
    def __init__(self, value):
        self.nodes = []
        self.value = value
        self.size = 0
    def add(c, elem):
        self.size+=c
        self.nodes.append(elem)
    def __len__(self):
        return self.size

def create_tree_helper(depth, last, ma1):
    if depth == 0:
        leaf = Node("/n")
        return leaf

    tset = set(ma1[last])
    node = Node(last)

    for elem in tset:
        inner = create_tree_helper(depth-1, elem, ma1)
        node.add(ma1[last].count(elem), inner) 

    return node





def crack(password, tests, num_processes, generator, verbose = False):
    signal.signal(signal.SIGINT, signal_handler)

    print create_tree(3, generator)
    sys.exit(0)
    generator.min_size = len(password)
    generator.max_size = len(password)
    maxcount = 26**len(password)
    count_index = maxcount / 100
    tlist = []
    plist = []

    for n in xrange(tests):
        processes = []
        count = 0
        print "Test",n

        q = multiprocessing.Queue()

        

        for x in xrange(num_processes):
            p = multiprocessing.Process(target = run, args=(generator, q))
            processes.append(p)

        for p in processes:
            p.start()

        if verbose:
            t0 = time.time()
            while q.get() != password:
                count+=1
                if count % (count_index/100) == 0:
                    sys.stdout.write("\r%f%%" %((float)(count)/(float)(maxcount)*100.0))
                    sys.stdout.flush()
            t1 = time.time()
            tlist.append(t1-t0)
            plist.append((float)(count)/(float)(maxcount))
            for elem in processes:
                elem.terminate()
            print
            print count

        else:
            t0 = time.time()
            while q.get() != password:
                count+=1
            t1 = time.time()
            tlist.append(t1-t0)
            plist.append((float)(count)/(float)(maxcount))
            for elem in processes:
                elem.terminate()

    average_time = sum(tlist)/len(tlist)
    average_percent = sum(plist)/len(plist)

    if verbose:
        print "Average time:\t\t\t", average_time
        print "Average percent searched:\t", average_percent

    with open("output/"+str(password)+"_"+str(tests)+".txt", "w") as f:
        out = "Testing password "+ str(password) +" "+ str(tests)+" times\n"
        f.write(out)

        total = zip(tlist, plist)

        for i, elem in enumerate(total):
            out = str(i) +"\t"+str(elem[0])+"\t"+str(elem[1])+"\n"
            f.write(out)
        f.write( "Average time:\t\t\t"+ str(average_time))
        f.write("Average percent searched:\t"+ str(average_percent))

