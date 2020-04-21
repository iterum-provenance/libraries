from typing import List

class LocalFileDesc:
    def __init__(self, name:str, path:str):
        self.name = name
        self.path = path


class LocalFragmentDesc:
    def __init__(self, files:List[LocalFileDesc]):
        self.files = files