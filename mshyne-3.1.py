import sys, os

directory_key = {}

# Check for correct number of arguments.
if not len(sys.argv) == 5:
	print "Not enough arguments provided. \n \n Please use the following input criteria: \n $./list_files.py --dir='testdir' --by=mtime --results=4 --direction='descending'"
	exit()

# Check that directory argument is actually a directory.
#try:
#	test_var = sys.argv[1].open()
#except NameError: 
#	print "Directory argument is a file. Please feed this program only a directory."
#	exit()
#except AttributeError:
#	print "All good. Continuing to process directory ..."

def processDirectory(directory):
	big_ole_dict = {}
	file_names = []
	for file in os.listdir(directory):
		fullpath = os.path.join(directory,file)
		if os.path.isfile(fullpath):
			if not file == ".DS_Store":
				file_names.append(file)
	if len(file_names) < result_number:
		print "There are not enough files in this directory to satisfy your desired result number. Please enter a number equal to or less than " + str(len(file_names))
		exit()
	else:
		for file in file_names:
			fullpath = os.path.join(directory,file)
			print fullpath
			file_size = os.stat(fullpath).st_size
			file_modified = os.stat(fullpath).st_mtime
			big_ole_dict[file] = { 'name': file, 'mtime': file_modified, 'size': file_size}
	print big_ole_dict
			
			
			#file_names.append(fullpath)
			#file_size = fullpath.st_size
			#file_modified = fullpath.st_mtime
			
	#print file_names

directory = sys.argv[1]
sort_criteria = sys.argv[2]
result_number = int(sys.argv[3])
sort_direction = sys.argv[4]

valid_criteria = (['mtime','size','name'])


# Argument validation.
if not sort_direction == "ascending" or sort_direction == "descending":
	print "Invalid value for sort direction. Please enter either 'ascending' or 'descending'."
	exit()
	
if not sort_criteria in valid_criteria:
	print "Invalid sort criteria. Please enter either 'mtime' (modified time), 'size' (file size), or 'name' (filename)."
	exit()

if result_number > len(os.listdir(directory)):
	print "Desired result number is higher than files in directory. Please enter an integer equal to or less than " + str(len(os.listdir(directory)))
	exit()

try:
	processDirectory(directory)
except OSError: 
	print "Directory argument is a file. Please feed this program only directories."
	exit()

#print directory