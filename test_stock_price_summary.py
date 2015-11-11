import stock_price_summary as sps

# TESTS FOR ACQUIRE_DATA
def test_good_arguments():
	assert sps.acquire_data('../stock_prices/AAPL.csv', 5) == [114.71, 115.0, 114.32, 113.4, 115.21]

def test_unreadable_file():
	assert sps.acquire_data('../data-input.py', 5) == [114.71, 115.0, 114.32, 113.4, 115.21]

def test_not_a_file():
	assert sps.acquire_data('AAPL', 5) == [114.71, 115.0, 114.32, 113.4, 115.21]

def test_entries_exceed():
	assert sps.acquire_data('../stock_prices/AAPL.csv', 255)

def test_entries_exceed_alt():
	assert sps.acquire_data('../stock_prices/AAPL.csv', 4) == [114.71, 115.0, 114.32, 113.4, 115.21]

def test_entries_exceed_alt2():
	assert sps.acquire_data('../stock_prices/AAPL.csv', 6) == [114.71, 115.0, 114.32, 113.4, 115.21]

def test_alt_files():
	assert sps.acquire_data('../stock_prices/fb.csv', 5) == [114.71, 115.0, 114.32, 113.4, 115.21]


# TESTS FOR IS_ALL_NUMBERS
def test_is_all_numbers():
	assert sps.is_all_numbers([1,3])

def test_is_list_of_many():
	assert sps.is_all_numbers([1,[1,4]])
	
def test_non_iterable():
	assert sps.is_all_numbers(5)
	

#TESTS FOR GET_MEDIAN
def test_get_median_not_iterable():
	assert sps.get_median(5)

def test_get_median_not_iterable_string():
	assert sps.get_median([114.71, 115.0, 114.32, 113.4, 'me'])

def test_get_median_even():
	assert sps.get_median([114.71, 115.0, 114.32, 113.4]) == 114.51499999999999

def test_get_median_odd():
	assert sps.get_median([114.71, 115.0, 114.32, 113.4, 113.7]) == 114.32
	
#TESTS FOR GET_CENTERED
def test_get_centered_not_iterable():
	assert sps.get_centered(5)

def test_get_centered_not_iterable():
	assert sps.get_centered([114.71, 115.0, 114.32, 113.4, 'me'])

def test_get_centered_duplicates():
	assert sps.get_centered([114.71, 115.0, 114.32, 113.4, 114.71]) == 114.51499999999999

def test_get_centered_top_and_bottom_duplicates():
	assert sps.get_centered([114.71, 115.0, 114.32, 113.4, 113.4, 115.0]) == 114.51499999999999

def test_get_centered_regular_list():
	assert sps.get_centered([114.71, 115.0, 114.32, 113.4, 115.21]) == 114.71
	
#TESTS FOR GET_AVERAGE
def test_get_average_not_iterable():
	assert sps.get_average(10)

def test_get_average_not_number():
	assert sps.get_average([114.71, 115.0, 114.32, 113.4, 'me'])

def test_get_average():
	assert sps.get_average([114.71, 115.0, 114.32, 113.4]) == 114.35749999999999
	
#TESTS FOR GET_FILENAME_FROM_TICKER
def test_get_filename_from_ticker_argtype():
	assert sps.get_filename_from_ticker(199)

def test_get_filename_from_ticker_uppercase():
	assert sps.get_filename_from_ticker('APPL')

def test_get_filename_from_ticker_lowercase():
	assert sps.get_filename_from_ticker('appl')