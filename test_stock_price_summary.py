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

def test_is_all_numbers():
	assert sps.is_all_numbers([1,3])