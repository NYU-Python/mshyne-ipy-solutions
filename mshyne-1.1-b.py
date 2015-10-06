import sys

# Get our working variables.
summary_type = str(sys.argv[1])
number_of_days = float(sys.argv[2])
stock_data_raw = open(sys.argv[3])


def validateSummary():
	if (summary_type == "max") or (summary_type == "min") or (summary_type == "average") or (summary_type == "centered") or (summary_type == "median"):
		return True
	else:
		return False

def makeDataDict():
	parsed_data = []

	for stock in stock_data_raw:
		data_line = stock.split(',')
		parsed_data.append(data_line)

	data_list = []

	header1 = parsed_data[0][0]
	header2 = parsed_data[0][1]
	header3 = parsed_data[0][2]
	header4 = parsed_data[0][3]
	header5 = parsed_data[0][4]
	header6 = parsed_data[0][5]

	parsed_data.pop(0)

	for line in parsed_data:
		dictionary_line = {}
		for data in line:
			if line.index(data) == 0:
				dictionary_line.update({header1:data})
			if line.index(data) == 1:
				dictionary_line.update({header2:data})
			if line.index(data) == 2:
				dictionary_line.update({header3:data})
			if line.index(data) == 3:
				dictionary_line.update({header4:data})
			if line.index(data) == 4:
				dictionary_line.update({header5:data})
			if line.index(data) == 5:
				dictionary_line.update({header6:data})
		data_list.append(dictionary_line)
	
	return data_list


def getMax(data_list):
	bottom = 0
	desired_data = []
	while bottom < number_of_days:
		integer_bottom = int(bottom)
		print data_list[integer_bottom]["Close"]
		desired_data.append(data_list[integer_bottom]["Close"])
		bottom = bottom + 1
	print max(desired_data)
	
def getMin(data_list):
	bottom = 0
	desired_data = []
	while bottom < number_of_days:
		desired_data.append(float(data_list[bottom]["Close"]))
		bottom = bottom + 1
	print min(desired_data)

def getAverage(data_list):
	bottom = 0
	desired_data = []
	while bottom < number_of_days:
		desired_data.append(float(data_list[bottom]["Close"]))
		bottom = bottom + 1
	print sum(desired_data) / number_of_days

def getMedian(data_list):
	bottom = 0
	desired_data = []
	while bottom < number_of_days:
		desired_data.append(float(data_list[bottom]["Close"]))
		bottom = bottom + 1
	sorted_data = sorted(desired_data)
	#if len(sorted_data) % 2:
	#	middleNumber = int((float(len(sorted_data))/2)) + 1
	if (int(number_of_days) % 2):
		middle_number = int(number_of_days/2) + 1
		print sorted_data[middle_number]
	else:
		middle_first = int(number_of_days/2)
		middle_second = int(number_of_days/2) + 1
		print (sorted_data[middle_first] + sorted_data[middle_second])/2

def getCentered(data_list):
	bottom = 0
	desired_data = []
	#print data_list[1]
	while bottom < number_of_days:
		#print (data_list[bottom]['Close'])
		desired_data.append(float(data_list[bottom]['Close']))
		bottom = bottom + 1
	sorted_data = sorted(desired_data)
	sorted_data.pop(0)
	sorted_data.pop(len(sorted_data))
	for data in sorted_data:
		next_index = sorted_data.index(data) + 1
		next_data = sorted_data[next_index]
		if data == next_data:
			sorted_data.pop(sorted_data.index(data))
	if (int(len(sorted_data)) % 2):
		middle_number = int(len(sorted_data)/2) + 1
		print sorted_data[middle_number]
	else:
		middle_first = int(len(sorted_data)/2)
		middle_second = int(len(sorted_data)/2) + 1
		print (sorted_data[middle_first] + sorted_data[middle_second])/2
	

#def getCentered(data_list):
#	bottom = 0
#	desired_data =


# Validate. Return errors if bad, process data if good.
if number_of_days > 251:
	print "Error: " + number_of_days + " is more than available in data source. \n Usage: ./stock_price_summary.py [summary type] [# of days] [ticker]"
elif validateSummary() == False:
	print "type " + summary_type + " not found \n Usage: ./stock_price_summary.py [summary type] [# days] [ticker]"
else:
	masterDataList = makeDataDict()
	if summary_type == "max":
		getMax(masterDataList)
	if summary_type == "min":
		getMin(masterDataList)
	if summary_type == "average":
		getAverage(masterDataList)
	if summary_type == "median":
		getMedian(masterDataList)
	if summary_type == "centered":
		getCentered(masterDataList)


		
