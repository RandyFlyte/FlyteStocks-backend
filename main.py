import yfinance as yf

msft = yf.Ticker("AMC231103C00009000")
# msft = yf.Ticker("MSFT")
print(msft.info)
# get all stock info
# msft.info

# get historical market data
# hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
# msft.history_metadata

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates

# show options expirations
#opt = msft.options
#print(opt)
# get option chain for specific expiration
amc = yf.Ticker("AMC")
opt = amc.option_chain('2023-10-20')
# Filter out unwanted fields from calls and puts
filtered_calls = [{key: option[key] for key in ['contractSymbol', 'strike']} for option in opt.calls.to_dict(orient='records')]
filtered_puts = [{key: option[key] for key in ['contractSymbol', 'strike']} for option in opt.puts.to_dict(orient='records')]

print(filtered_calls)
#calls = opt.calls.to_dict(orient='records')
#puts = opt.puts.to_dict(orient='records')
#print(calls)

# data available via: opt.calls, opt.puts