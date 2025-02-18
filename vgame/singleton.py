__all__ = ["Singleton"]

from typing import Self


class Singleton:
    __lock = False

    @classmethod
    def clear_lock(cls) -> None:
        """Clear the instance lock"""
        cls.__lock = False

    def __new__(cls) -> Self:
        if cls.__lock:
            msg = "Can only create one instance of class"
            raise RuntimeError(msg)
        cls.__lock = True
        return object.__new__(cls)

    def __del__(self) -> None:
        self.__class__.clear_lock()
