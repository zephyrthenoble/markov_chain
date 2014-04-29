markov_chain
============

Create a Markov chain


This Python 2 module creates a Markov by reading in text and calculating probabilities.

First, determine what you wish to test.  We have two example Markov chain uses:

1. A text generator that uses written prose to generate similar sentences
2. A password "cracker" that takes an input password and number of tests


The markov module contains everything to run these cases in one script, but for
ease of use we will create a Generator object first, and then pickle it to use
later.

Read each section below to learn how to do each example.

Text Generator
--------------

Execute
python2 write.py

Enter the text you are parsing (text.txt)

Then run
python2 run.py

Enter the pickle you are using (text.pickle)

Look at the output, a sorted list of 1000 generated sentences!
Examine the code in write.py and run.py to see how this works

Password Cracker
----------------

Warning: on a fast computer, it takes about 10 seconds to crack a 5 letter
password.  Try small passwords and a small number of tests initially.

Execute
python2 write_pw.py

Enter the password file (passwords.txt)

Then run
python2 password_cracker.py

Enter the password you are trying to crack
Enter the number of tests

The code will print out the test number and the percent of the state space
searched.
