from typing import List

from pyterum.socket_conn import SocketConn
from pyterum import env

class FragmenterInput(SocketConn):

    def __init__(self, address:str=None):
        address = env.FRAGMENTER_INPUT if address == None else address
        super().__init__(address, retry_policy={"consume": 0})

        print(f"Initializing FragmenterInput...", flush=True)
        self.connect()
        self.produce = None
        self._consumer = super().consumer()

    def consumer(self) -> List[str]:
        while True:
            yield next(self._consumer)


class FragmenterOutput(SocketConn):

    def __init__(self, address:str=None):
        address = env.FRAGMENTER_OUTPUT if address == None else address
        super().__init__(address, retry_policy={"produce": 0})

        print(f"Initializing FragmenterOutput...", flush=True)
        self.connect()
        self.consumer = None

    def produce(self, data:List[str]):
        super().produce(data)