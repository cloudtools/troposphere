"""Type definition backward compatibility."""
# flake8: noqa
from __future__ import annotations

import sys

if sys.version_info < (3, 8):  # 3.7
    from typing_extensions import Final, Literal, Protocol, SupportsIndex
else:
    from typing import Final, Literal, Protocol, SupportsIndex
