from __future__ import annotations


class Texture:
    file: str
    size: tuple[int, int]

    def __init__(self, file: str, size: tuple[int, int]) -> None:
        self.file = file
        self.size = size

    @property
    def id(self) -> str:
        return f"{self.file}_{self.size}"
