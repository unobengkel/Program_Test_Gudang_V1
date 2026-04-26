from abc import ABC, abstractmethod
from typing import Any


class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Any:
        pass

    @abstractmethod
    def create(self, data: Any) -> int:
        pass

    @abstractmethod
    def update(self, id: int, data: Any) -> bool:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
