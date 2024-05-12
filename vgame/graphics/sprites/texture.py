class Texture:
    def __init__(self, file: str, size: tuple[float, float]) -> None:
        self.file = file
        self.size = size

    @property
    def id(self) -> str:
        return f"{self.file}_{self.size}"
