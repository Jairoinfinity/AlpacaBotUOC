from alpacaConnection import AlpacaConnection
from wsc import WSC_Client as wsc
import setup_config as sc

wsc.connectToAlpaca('wss://stream.data.alpaca.markets/v2/iex')


"""
ac = AlpacaConnection(sc.API_KEY, sc.SECRET_KEY, sc.BASE_URL)

ac.connect()
print(ac.getHistoricalDataMarkets(15,"Min", "AAPL", "2018-10-12", "2019-10-12"))
"""
