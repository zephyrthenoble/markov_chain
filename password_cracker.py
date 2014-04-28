
import sys,  pickle
from multiprocessing import cpu_count
from markov.generator import Generator
from markov import password_cracker

def main():

    password = raw_input("Enter your password: ")

    if password == "":
        password = "test"

    cores = cpu_count()-1
    if cores <= 0:
        cores = 1
    gen = Generator.load("dictionaries/passwords.pickle")
    try:
        tests = int(raw_input("Enter number of tests: "))
    except:
        tests = 10
    print "Running",tests,"tests for", password
    password_cracker.crack(password, tests, cores, gen, True)

if __name__ == "__main__":
    main()
