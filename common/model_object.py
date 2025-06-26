

from abc import ABC
from typing import Any, override
import uuid


class ModelObject(ABC):

    __slots__ = ()

    def __init__(self, id: str | None = None) -> None:
        self.__set_id(id)

    @property
    def id(self) -> str:
        return str(self.__id)
    
    def __set_id(self, value: str | None) -> None:
        self.__id: uuid.UUID = uuid.UUID(value) if value else uuid.uuid4()


    @override
    def __repr__(self) -> str:
        return f"id='{self.id}'"


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.__set_id(kwds['id'])

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return False
        
        return self.id == value.id
    
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    