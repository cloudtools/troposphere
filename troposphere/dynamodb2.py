from .dynamodb import *  # NOQA

import warnings

warnings.warn("This module has replaced troposphere.dynamodb. Please use that "
              "module instead, as troposphere.dynamodb2 will be being removed "
              "soon.")
