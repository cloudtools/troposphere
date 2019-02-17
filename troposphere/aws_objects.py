"""Base AWS Objects"""

import troposphere.validators as validators
from typing import Dict


class AWSObject():
    pass


class AWSProperty(AWSObject):
    pass


class AWSResource(AWSObject):
    def __init__(self, logical_name: str):
        self.logical_name: str = None

        self.properties: Dict[str, AWSProperty] = {}

    @property
    def logical_name(self) -> str:
        return self._logical_name

    @logical_name.setter
    def logical_name(self, logical_name: str) -> None:
        validators.alphanumeric(logical_name)
        self._logical_name = logical_name
