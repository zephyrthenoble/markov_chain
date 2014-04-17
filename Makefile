default:
	python2 run.py
clean:
	rm -rf markov/*.pyc
	rm -rf dictionaries/*.pickle
write:
	python2 write.py
debug:
	python2 run.py debug
