"""Data container for field validation in properties and resources



"""

from typing import Dict

class ValidatorData():
    def __init__(self, validatordata: Dict):
        self.parse(validatordata)

        self.validator: BaseValidator = None


    def parse(self, validatordata: Dict):
        validatormap = {
            "regex": RegexValidator,
            "Map": MapValidator,
        }


class BaseValidator:
    pass

class RegexValidator(BaseValidator):
    def __init__(self, validatordata: Dict):
        pass

class MapValidator(BaseValidator):
    pass
