import json
from ws4py.client.threadedclient import WebSocketClient
import setup_config as sc

class WSC_Client(WebSocketClient):

    def opened(self):
        req = {
            "action": "auth",
            "key": sc.API_KEY,
            "secret": sc.SECRET_KEY
        }
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        data = resp['data']
        if type(data) is dict:
            ask = data['asks'][0]
            print('Ask:', ask)
            bid = data['bids'][0]
            print('Bid:', bid)

    def connect(url):
        if __name__ == '__main__':
            ws = None
            try:
                ws = WSC_Client(url)
                ws.connect()
                ws.run_forever()
                ws.opened()
            except KeyboardInterrupt:
                ws.close()