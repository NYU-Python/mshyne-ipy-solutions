import flask
import urllib
import os

DATABASE = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=a'

app = flask.Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
	return flask.render_templates('flask_home.html') 

@app.route('/display_data')            #decorator indicates web URL
def display_data():
	user_ticker = flask.session['ticker']
	stock_price = build_stockprice(user_ticker)
	return flask.render_template('flask_stock_price.html', ticker=user_ticker, price=stock_price)	

@app.route('/get_stock')
def get_stock():
	flask.session['ticker'] = flask.request.values['ticker']
	return flask.redirect(flask.url_for('display_data'))

def build_stockprice(stock_ticker):
	database = DATABASE.format(stock_ticker)
	stock_price = urllib.urlopen(database).read().rstrip('\n')
	return stock_price


if __name__ == '__main__':
    app.run(debug=True)              # app starts serving

#stock_price = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s=AAPL&f=a').read().rstrip('\n')

#print stock_price