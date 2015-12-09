import flask
import urllib
import os

YAHOO_API = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=a'

app = flask.Flask(__name__) 

@app.route('/')
def index():
	return flask.render_template('flask_home.html') 

@app.route('/get_stock', methods=['POST'])            #decorator indicates web URL
def get_stock():
	user_ticker = flask.request.form['ticker']
	stock_price = build_stockprice(user_ticker)
	return flask.render_template('flask_stock_price.html', ticker=user_ticker, price=stock_price)	

def build_stockprice(stock_ticker):
	api_link = YAHOO_API.format(stock_ticker)
	stock_price = urllib.urlopen(api_link).read().rstrip('\n')
	return stock_price


if __name__ == '__main__':
    app.run(debug=True)              # app starts serving
