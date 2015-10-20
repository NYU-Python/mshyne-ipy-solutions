import sys, os

sort_type = sys.argv[1]
raw_data = open(sys.argv[2])

datadict = {}

if sort_type == "cities":
	cities = []
	
	for line in raw_data.readlines()[1:]:
		line_list = line.split('\t')
		for field in line_list:
			if line_list.index(field) == 3:
				if not field == '':
					cities.append(field)
		
	for city in sorted(set(cities),key=str.lower):
		print city	