import sys

number_of_days = float(sys.argv[1])
stock_data_raw = open(sys.argv[2])

parsed_data = []

#data_time = stock_data.readlines()
#print stock_data

for stock in stock_data_raw:
	data_line = stock.split(',')
	parsed_data.append(data_line)
	#if data_line[1] == 'Open': 
	#	continue
	#else:
	#	parsed_data.append(data_line)


parsed_data.pop(0)

bottom = 0
desired_data = []

while bottom < number_of_days:
	desired_data.append(float(parsed_data[bottom][4]))
	bottom = bottom + 1
	
print sum(desired_data) / number_of_days