import json
from ws4py.client.threadedclient import WebSocketClient
import setup_config as sc

class WSC_Client(WebSocketClient):

    def opened(self):
        req = '{ "action": "auth", "key": "PK6Y2YCCY7U3WJZSIMOU", "secret": "xJXxdvDDblwkGUmoaEmRFVi1LRG1npcSPPwgnALq" }'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        print(resp)
