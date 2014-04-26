
default:
	python2 run.py
clean:
	rm -rf markov/*.pyc
	rm -rf dictionaries/*.pickle

test:

text:
	python2 write.py text

password: write

write:
	python2 write.py
debug:
	python2 run.py debug
