import os, sys, timeit

fh = sys.argv[1]

def forloop(fh):
	my_list = []
	file = open(os.path.abspath(fh))
	for line in file.readlines():
		lowercase_line = (line.rstrip('".,;:?!\n\'')).lower()
		my_list.append(lowercase_line)

def listcomp(fh):
	my_list = [(i.rstrip('".,;:?!\n\'')).lower() for i in (open(os.path.abspath(fh))).readlines()]

def gencomp(fh):
	generator = ((i.rstrip('".,;:?!\n\'')).lower() for i in (open(os.path.abspath(fh))).readlines())
	my_list = list(generator)

def mapping(fh):
	my_list = map(lambda x: x.rstrip('".,;:?!\n\'').lower(), (open(os.path.abspath(fh))).readlines())

print timeit.timeit('forloop(fh)', setup='from __main__ import forloop, fh', number=10)
print timeit.timeit('listcomp(fh)', setup='from __main__ import listcomp, fh', number=10)
print timeit.timeit('gencomp(fh)', setup='from __main__ import gencomp, fh', number=10)
print timeit.timeit('mapping(fh)', setup='from __main__ import mapping, fh', number=10)