import sys

number_of_days = int(sys.argv[1])
stock_data_raw = open(sys.argv[2])

parsed_data = []


for stock in stock_data_raw.readlines()[1:number_of_days]:
	data_line = stock.split(',')
	parsed_data.append(float(data_line[4]))

	
print sum(parsed_data) / number_of_days