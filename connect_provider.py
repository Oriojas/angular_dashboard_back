import os
from web3 import Web3

WS = os.environ["WS"]


class test_Provider:

    def __init__(self):
        self.w3 = Web3(Web3.WebsocketProvider(f"{WS}"))

    def connected(self):
        con = self.w3.is_connected()

        return con

    def info(self):
        info = dict(self.w3.eth.get_block('latest'))

        return info
