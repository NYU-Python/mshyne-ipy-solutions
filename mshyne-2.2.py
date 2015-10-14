import sys
import os

sort_type = sys.argv[1]
raw_data = open(sys.argv[2])


datadict = {}


if sort_type == "cities":
	data_list = []
	keys = []
	cities = []
	
	for line in raw_data:
		data_line = line.split('\t')
		data_list.append(data_line)

	for line in data_list[0]:
		keys.append(line)
		
	for line in data_list[1:len(data_list)]:
		for info in line:
			if line.index(info) == keys.index("geo_city_name"):
				if not info == '':
					cities.append(info)
				if line.index(info) == len(line):
					break
					
	for city in sorted(list(set(cities)),key=str.lower):
		print city
		
	
	#for line in raw_data[0]:
	#	data_line = line.split('\t')
	#	print data_line
#		data_dict_line = {}
#		if line == raw_data[0]:
#			keys = line
#		else:
#			for data in data_line:
#				if data_line.index(data) == keys.index("geo_city_name"):
#					if not data == "":
#						cities.append(data)
#	print set(cities.sorted())
		