
from enum import Enum



class FormResult(Enum):
    CLOSE = 0
    BACK = 1
    CANCEL = 2
    SAVE = 4
    EDIT = 5
    RUNNING = 6

class FormAction(Enum):
    CREATE = 0
    UPDATE = 1

class State(Enum):
    ERROR = 0
    SUCCESS = 1



class Message:
    def __init__(self, field: str, value: str) -> None:
        self.field = field
        self.value = value

    @property
    def field(self) -> str:
        return self.__field
    
    @field.setter
    def field(self, value: str) -> None:
        self.__field: str = value


    @property
    def value(self) -> str:
        return self.__value
    
    @value.setter
    def value(self, value: str) -> None:
        self.__value: str = value



class MethodResult:
    def __init__(self, state: State, *message: Message, return_data: object = None) -> None:
        self.__state = state
        self.__message = message
        self.__return_data = return_data

    @property
    def state(self) -> State:
        return self.__state
    
    @property
    def message(self) -> tuple[Message]:
        return self.__message
    
    @property
    def return_data(self) -> object:
        return self.__return_data
