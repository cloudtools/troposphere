"""Data container for field validation in properties and resources



"""

from typing import Dict

class ValidatorData():
    def __init__(self, validatordata: Dict):
        self.parse(validatordata)


    def parse(self, validatordata: Dict):
        pass
