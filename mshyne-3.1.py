import sys, os, time

## MAIN FUNCTIONS
# Process directory files into a dictionary containing the number of files the user specified.
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

# Get sorted modified time from dictionary made in process_dictionary.
def get_mtime(processed_directory):
	data_desired = []
	for file in processed_directory:
		data_desired.append((processed_directory[file]['name'],int(processed_directory[file]['mtime'])))
	if sort_direction == 'ascending':
		return sorted(data_desired, key=lambda tup: tup[1])
	else:
		return sorted(data_desired, key=lambda tup: tup[1], reverse=True)

# Get sorted file size from dictionary made in process_dictionary.		
def get_file_size(processed_directory):
	data_desired = []
	for file in processed_directory:
		data_desired.append((processed_directory[file]['name'],int(processed_directory[file]['size'])))
	if sort_direction == 'ascending':
		return sorted(data_desired, key=lambda tup: tup[1])
	else:
		return sorted(data_desired, key=lambda tup: tup[1], reverse=True)	

# Check for correct number of arguments.

if '-h' in sys.argv:
	print """The following convention should be used to make use of this program:
	
$ ./mshyne-3.1py ./directory sort_by result_number sort_direction

arguments:
	sort_by: valid arguments 'name' (sort by file name), 'size' (sort by file size), and 'mtime' (sort by last date modified)
	result_number: how many items should be sorted from the ./directory. valid integers only.
	sort_direction: valid arguments 'ascending' (sort by ascending value), 'descending (sort by descending value)

optional argument:
	-h: show this help message and exit
	"""
	exit()
if not len(sys.argv) == 5:
	print "Not enough arguments provided. \n \n Please use the following input criteria: \n $./list_files.py --dir='testdir' --by=mtime --results=4 --direction='descending'"
	exit()

# Collect arguments into global variables.
directory = sys.argv[1]
sort_criteria = sys.argv[2]
try:
	result_number = int(sys.argv[3])
except ValueError:
	print "Invalid value for result_number. Please enter an integer."
	exit()
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
		print "Last Modified: %s" % time.ctime(data[1])
if sort_criteria == "size":
	data_sorted = get_file_size(processed_directory)
	for data in data_sorted:
		print data[0]
		print "Size: %s bytes" % data[1]
if sort_criteria == "name":
	data = []
	for key in processed_directory:
		data.append(processed_directory[key]['name'])
	if sort_direction == "ascending":
		for item in sorted(data):
			print item
	if sort_direction == "descending":
		for item in sorted(data, reverse=True):
			print item
	