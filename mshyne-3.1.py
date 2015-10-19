import sys, os

directory_key = {}

# Check for correct number of arguments.
if not len(sys.argv) == 5:
	print "Not enough arguments provided. \n \n Please use the following input criteria: \n $./list_files.py --dir='testdir' --by=mtime --results=4 --direction='descending'"
	exit()

def process_directory(directory):
	big_ole_dict = {}
	file_names = []
	for file in os.listdir(directory):
		fullpath = os.path.join(directory,file)
		if os.path.isfile(fullpath):
			if not file == ".DS_Store":
				if len(file_names) < result_number:
					file_names.append(file)
	if len(file_names) < result_number:
		print "There are not enough files in this directory to satisfy your desired result number. Please enter a number equal to or less than " + str(len(file_names))
		exit()
	else:
		for file in file_names:
			fullpath = os.path.join(directory,file)
			big_ole_dict[file] = { 'name': os.path.basename(fullpath), 'mtime': os.stat(fullpath).st_mtime, 'size': os.stat(fullpath).st_size}
	return big_ole_dict

def get_mtime(processed_directory):
	data_desired = []
	for file in processed_directory:
		data_desired.append((processed_directory[file]['name'],int(processed_directory[file]['mtime'])))
	if sort_direction == 'ascending':
		return sorted(data_desired, key=lambda tup: tup[1])
	else:
		return sorted(data_desired, key=lambda tup: tup[1], reverse=True)
	#return data_desired

directory = sys.argv[1]
sort_criteria = sys.argv[2]
result_number = int(sys.argv[3])
sort_direction = sys.argv[4]

valid_criteria = {'sort_criteria':(['mtime','size','name']), 'sort_direction':(['ascending','descending'])}


# Argument validation.
if not sort_direction in valid_criteria['sort_direction']:
	print "Invalid value for sort direction. Please enter either 'ascending' or 'descending'."
	exit()
	
if not sort_criteria in valid_criteria['sort_criteria']:
	print "Invalid sort criteria. Please enter either 'mtime' (modified time), 'size' (file size), or 'name' (filename)."
	exit()

if result_number > len(os.listdir(directory)):
	print "Desired result number is higher than files in directory. Please enter an integer equal to or less than " + str(len(os.listdir(directory)))
	exit()

try:
	processed_directory = process_directory(directory)
except OSError: 
	print "Directory argument is a file. Please feed this program only directories."
	exit()


if sort_criteria == "mtime":
	data_sorted = get_mtime(processed_directory)
	for data in data_sorted:
		print data[0]