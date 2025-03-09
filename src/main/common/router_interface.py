from abc import ABC, abstractmethod
from typing import Any


class AbstractRouter(ABC):

    @abstractmethod
    async def get_object(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    async def get_objects(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    async def create_object(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    async def update_object(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    async def delete_object(self, *args, **kwargs) -> Any:
        pass
