from typing import List

from pyterum.socket_conn import SocketConn
from pyterum.local_fragment_desc import LocalFragmentDesc
from pyterum import env

class TransformationStepInput(SocketConn):

    def __init__(self, address:str=None):
        address = env.TRANSFORMATION_STEP_INPUT if address == None else address
        super().__init__(address, retry_policy={"consume": -1})

        print(f"Initializing TransformationStepInput...", flush=True)
        self.connect()
        self.produce = None
        self._consumer = super().consumer()

    def consumer(self) -> LocalFragmentDesc:
        yield next(self._consumer)


class TransformationStepOutput(SocketConn):

    def __init__(self, address:str=None):
        address = env.TRANSFORMATION_STEP_OUTPUT if address == None else address
        super().__init__(address, retry_policy={"produce": 0})

        print(f"Initializing TransformationStepOutput...", flush=True)
        self.connect()
        self.consumer = None

    def produce(self, data:LocalFragmentDesc):
        super().produce(data)