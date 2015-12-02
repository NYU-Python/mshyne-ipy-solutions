import os, sys, timeit

def strip_punct(line):
	punctuation = ["'", ":", ";", "?", "!", ".", ","]
	for mark in punctuation:
		if mark in line:
			line = line.replace(mark, "")
	line = (line.strip("\n")).lower()
	return line

def forloop(fh):
	my_list = []
	file = open(os.path.abspath(fh))
	for line in file.readlines():
		lowercase_line = strip_punct(line)
		my_list.append(lowercase_line)
	print my_list

def listcomp(fh):
	my_list = [strip_punct(i) for i in (open(os.path.abspath(fh))).readlines()]
	print my_list

def gencomp(fh):
	generator = (strip_punct(i) for i in (open(os.path.abspath(fh))).readlines())
	my_list = list(generator)
	print my_list

def mapping(fh):
	my_list = map(strip_punct, (open(os.path.abspath(fh))).readlines()) 
	print my_list

#mapping(sys.argv[1])

timeit.timeit('forloop(sys.argv[1])', setup='from __main__ import forloop, strip_punct', number=10000)