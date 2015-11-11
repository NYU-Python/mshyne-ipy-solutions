import stock_price_summary as sps

def test_initial():
	assert sps.acquire_data(filename, 5) == [114.71, 115.0, 114.32, 113.4, 115.21]