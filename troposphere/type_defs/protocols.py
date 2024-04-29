"""Protocols."""

from __future__ import annotations

from typing import Any, Dict

from .compat import Protocol


class JSONreprProtocol(Protocol):
    def JSONrepr(self, *__args: Any, **__kwargs: Any) -> Dict[str, Any]:
        raise NotImplementedError


class ToDictProtocol(Protocol):
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError
