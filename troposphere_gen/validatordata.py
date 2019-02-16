"""Data container for field validation in properties and resources



"""

from typing import Dict

class ValidatorData():
    def __init__(self, validatordata: Dict):
        self.validators: Dict[str, PropertyValidator] = {}
        self.parse(validatordata)

    def parse(self, validatordata: Dict):
        for propname, validatordict in validatordata["Properties"].items():
            self.validators[propname] = PropertyValidator(validatordict)


class PropertyValidator():
    def __init__(self, validatordata: Dict):
        # Name of validator function and kwargs to be passed to it
        self.function: str = None
        self.kwargs: Dict[str, str] = {}

        # In case of a map we need a validator for both key and value
        self.map_key_function: str = None
        self.map_value_function: str = None
        self.map_key_kwargs: Dict[str, str] = {}
        self.map_value_kwargs: Dict[str, str] = {}

        self.parse(validatordata)

    def parse(self, validatordata: Dict):
        # 'Map' type validator is the only special case
        if validatordata["Validator"] == "Map":
            if "ValidatorKey" in validatordata:
                keydata = validatordata["ValidatorKey"]
                for k, v in keydata.items():
                    if k == "Validator":
                        self.map_key_function = v
                    else:
                        self.map_key_kwargs[k] = v

            if "ValidatorValue" in validatordata:
                valuedata = validatordata["ValidatorValue"]
                for k, v in valuedata.items():
                    if k == "Validator":
                        self.map_value_function = v
                    else:
                        self.map_value_kwargs[k] = v
        else:
            for k, v in validatordata.items():
                if k == "Validator":
                    self.function = v
                else:
                    self.kwargs[k] = v
