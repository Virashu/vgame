"""Controls axis"""
# alpha

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .keys import Keys


class Axis:
    def __init__(self, key_lower: Keys | int, key_upper: Keys | int) -> None:
        self.key_lower = key_lower
        self.key_upper = key_upper
        self.value = 0.0

    def update(self, keys: set[Keys | int]) -> None:
        self.value = 0
        if self.key_lower in keys:
            self.value -= 1
        if self.key_upper in keys:
            self.value += 1

    @property
    def axis(self) -> float:
        return self.value
