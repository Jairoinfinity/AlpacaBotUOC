import requests, json

class AlpacaConnection:

    # Atributos
    __API_KEY = ""
    __SECRET_KEY = ""
    __BASE_URL = ""
    __HEADERS = {}
    __ACCOUNT_URL = ""
    __ORDERS_URL = ""
    __DATA_URL = ""
    __PORTFOLIO = []

    # Constructor
    def __init__(self, apiKey, secretKey, url):
        self.__API_KEY = apiKey
        self.__SECRET_KEY = secretKey
        self.__BASE_URL = url
        self.__HEADERS = {'APCA-API-KEY-ID': self.__API_KEY, 'APCA-API-SECRET-KEY': self.__SECRET_KEY}
        self.__ACCOUNT_URL = "{}/v2/account".format(self.__BASE_URL)
        self.__ORDERS_URL = "{}/v2/orders".format(self.__BASE_URL)
    
    # Funciones Getters
    def getApiKey(self):
        return self.__API_KEY
    
    def getSecretKey(self):
        return self.__SECRET_KEY
    
    def getUrl(self):
        return self.__BASE_URL
    
    def getAccountUrl(self):
        return self.__ACCOUNT_URL

    def getOrdersUrl(self):
        return self.__ORDERS_URL
    
    def getPortfolio(self):
        return self.__PORTFOLIO

    # Funciones Setters
    def setApiKey(self, key):
        print(f"Old API_KEY: {self.__API_KEY}")
        self.__API_KEY = key
        print(f"New API_KEY: {self.__API_KEY}")
    
    def setSecretKey(self, key):
        print(f"Old SECRET_KEY: {self.__SECRET_KEY}")
        self.__SECRET_KEY = key
        print(f"New SECRET_KEY: {self.__SECRET_KEY}")
    
    def setUrl(self, url):
        print(f"Old APY_KEY: {self.__BASE_URL}")
        self.__BASE_URL = url
        print(f"New APY_KEY: {self.__BASE_URL}")
    
    def setAccountUrl(self, url):
        print(f"Old Account Url: {self.__ACCOUNT_URL}")
        self.__ACCOUNT_URL = url
        print(f"New Account Url: {self.__ACCOUNT_URL}")
    
    def setOrderstUrl(self, url):
        print(f"Old Orders Url: {self.__ORDERS_URL}")
        self.__ORDERS_URL = url
        print(f"New Orders Url: {self.__ORDERS_URL}")

    def setPortfolio(self, portfolio):
        print(f"Old Portfolio: {self.__PORTFOLIO}")
        self.__PORTFOLIO = portfolio
        print(f"New Portfolio: {self.__PORTFOLIO}")
    

    # Funciones
    """
    connect() es la función encargada de conectarnos a alpaca
    con nuestras credenciales.
    """
    def connect(self):
        try:
            rq = requests.get(self.__ACCOUNT_URL, headers=self.__HEADERS)
            return json.loads(rq.content)
        except:
            return "Error al conectarte al servidor."

    """
    getConfig() devuelve toda la información de la configuración
    """
    def getConfig(self):
        config = f"API_KEY: {self.__API_KEY}\n"
        config += f"SECRET_KEY: {self.__SECRET_KEY}\n"
        config += f"BASE_URL: {self.__BASE_URL}\n"
        config += f"HEADERS: {self.__HEADERS}\n"
        config += f"ACCOUNT_URL: {self.__ACCOUNT_URL}\n"
        config += f"ORDERS_URL: {self.__ORDERS_URL}\n"

        return config

    """
    createOrder() Realiza una operación en el mercado.

    # symbol: Símbolo o ID del activo para identificar el activo a negociar (EJ. “AAPL,TSLA,MSFT,EURUSD”).
    # qty: Número de acciones a negociar. Puede ser fraccionable sólo para los tipos de órdenes de mercado y del día.
    # side: Comprar o vender (EJ. buy, sell).
    # type: market, limit, stop, stop_limit, o trailing_stop
    # time_in_force: Tiempo que permanece una orden en el mercado (EJ. day, gtc, opg, cls, ioc, fok) Leer: https://alpaca.markets/docs/trading-on-alpaca/orders/#time-in-force
    """
    def createOrder(self, symbol, qty, side, type, time_in_force):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force
        }

        r = requests.post(self.__ORDERS_URL, json=data, headers=self.__HEADERS)

        return json.loads(r.content)
    
    """
    createOrderTpAndStp() Realiza una operación en el mercado con su take profit y stop loss.

    # symbol: Símbolo o ID del activo para identificar el activo a negociar (EJ. “AAPL,TSLA,MSFT,EURUSD”).
    # qty: Número de acciones a negociar. Puede ser fraccionable sólo para los tipos de órdenes de mercado y del día.
    # side: Comprar o vender (EJ. buy, sell).
    # type: market, limit, stop, stop_limit, o trailing_stop
    # time_in_force: Tiempo que permanece una orden en el mercado (EJ. day, gtc, opg, cls, ioc, fok) Leer: https://alpaca.markets/docs/trading-on-alpaca/orders/#time-in-force
    # limit_price: Precio de la orden limitada de take profit.
    # stop_loss: Precio de la orden limitada de stop loss.
    """
    def createOrderTpAndStp(self, symbol, qty, side, type, time_in_force, limit_price, stop_loss):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force,
            "order_class": 'bracket',
            "take_profit":{"limit_price": limit_price},
            "stop_loss": {"stop_loss": stop_loss}
        }

        r = requests.post(self.__ORDERS_URL, json=data, headers=self.__HEADERS)

        return json.loads(r.content)
    
    """
    getOrders() Devuelve los datos de todas las operaciones realizadas 
    """
    def getOrders(self):
        r = requests.get(self.__ORDERS_URL, headers=self.__HEADERS)
        return json.loads(r.content)
    
    
    """
    getLiveDataMarkets() Devuelve los datos de los mercados que seleccionemos en un portafolio(watchlists) en tiempo real.
    """
    # Fase de desarrollo o eliminación
    def getLiveDataMarkets(self):
        data = {"action":"subscribe","trades":[],"quotes":[],"bars":self.__PORTFOLIO}

        return data
    
    """
    getHistoricalDataMarkets() Devuelve los datos de los mercados que seleccionemos.

    # temp: El tiempo de cada vela.
    # timeframe: El valor de tiempo de las velas. (EJ. Min, Hour, Day).
    # symbols: Símbolo o ID del activo para identificar el activo a negociar (EJ. “AAPL,TSLA,MSFT,EURUSD”).
    # start: Fecha de inicio de los datos de mercado (EJ. 2019-10-12).
    # end: fecha de finalización de los datos de mercado (EJ. 2020-10-12).
    # limit: Número de puntos de datos a devolver. Debe estar en el rango 1-10000, por defecto es 1000.
    """

    # Aun en desarrollo
    def getHistoricalDataMarkets(self, temp, timeframe, symbol, start, end, limit=1000):
        data_url = "{}/v2/stocks/{}/bars".format(self.__BASE_URL, symbol)
        data = {
            "start": start,
            "end": end,
            "limit": limit,
            "timeframe": str(temp)+timeframe
        }

        r = requests.get(data_url, json=data, headers=self.__HEADERS)

        return r
    #---------------------------------