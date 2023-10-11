from flask import Flask, jsonify
import yfinance as yf
from flask_cors import CORS  # Import the CORS library

app = Flask(__name__)
CORS(app)  # Initialize the Flask-CORS extension with the default arguments

# Given a Symbol, return info on symbol.
@app.route('/info/<string:ticker_or_option>', methods=['GET'])
def get_info(ticker_or_option):
    asset = yf.Ticker(ticker_or_option)
    info = asset.info

    # Selecting some of the info to return
    selected_info = {key: info[key] for key in ['symbol', 'shortName', 'previousClose', 'open', 'dayLow', 'dayHigh'] if
                     key in info}

    return jsonify(selected_info)


# Given a Ticker, returns all expiration dates.
@app.route('/options/<string:ticker>', methods=['GET'])
def get_option_dates(ticker):
    asset = yf.Ticker(ticker)
    option_dates = asset.options
    return jsonify(option_dates)


# Given a Ticker and a Date, returns all contracts at date.
@app.route('/option_chain/<string:ticker>/<string:date>', methods=['GET'])
def get_option_chain(ticker, date):
    asset = yf.Ticker(ticker)
    option_chain = asset.option_chain(date)

    # Filter out unwanted fields from calls and puts
    filtered_calls = [{key: option[key] for key in ['contractSymbol', 'strike']} for option in
                      option_chain.calls.to_dict(orient='records')]
    filtered_puts = [{key: option[key] for key in ['contractSymbol', 'strike']} for option in
                     option_chain.puts.to_dict(orient='records')]

    return jsonify({
        'calls': filtered_calls,
        'puts': filtered_puts,
        'underlying': option_chain.underlying
    })


if __name__ == '__main__':
    app.run(debug=True)
