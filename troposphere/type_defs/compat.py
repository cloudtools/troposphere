"""Type definition backward compatibility."""
from __future__ import annotations

import sys

if sys.version_info < (3, 8):  # 3.7
    from typing_extensions import Literal, Protocol, SupportsIndex
else:
    from typing import Literal, Protocol, SupportsIndex
