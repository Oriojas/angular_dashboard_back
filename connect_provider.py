import os
from web3 import AsyncWeb3

URL = os.getenv("URL")


class test_Provider:

    def __init__(self):
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(URL))

    async def connected(self):
        con = self.w3.is_connected()

        return con

    async def info(self):
        info = dict(self.w3.eth.get_block('latest'))

        return info
