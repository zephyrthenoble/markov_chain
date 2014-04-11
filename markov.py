"""markov.py"""
password_file = "passwords.txt"

passwords = []
with open(password_file, 'r') as f:
    while f.hasNext():
        passwords.append( f.readline())
print passwords

