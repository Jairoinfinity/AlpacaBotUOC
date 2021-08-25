import json
from ws4py.client.threadedclient import WebSocketClient
import setup_config as sc

class WSC_Client(WebSocketClient):

    def opened(self):
        req = { "action": "auth", "key": sc.API_KEY, "secret": sc.SECRET_KEY }
        self.send(json.dumps(req))

        req = {"action":"subscribe","trades":[],"quotes":[],"bars":["AAPL","VOO"]}
        self.send(json.dumps(req))

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        print(resp)
