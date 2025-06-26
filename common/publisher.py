


from typing import override, Any
from common.model_object import ModelObject


class Publisher(ModelObject):
    __slots__ = ('_Publisher__name', '_Publisher__phone', '_Publisher__location', '_ModelObject__id')

    def __init__(self, name: str, phone: str, location: str, id: str | None = None) -> None:
        super().__init__(id=id)
        self.name = name
        self.phone = phone
        self.location = location

    # region name
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        self.__name: str = value # type: ignore
    #endregion

    # region phone
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, value: str) -> None:
        self.__phone: str = value # type: ignore
    #endregion

    # region location
    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, value: str) -> None:
        self.__location: str = value # type: ignore
    #endregion

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        super().__call__(*args, **kwds)

        if 'name' in kwds:
            self.name = kwds['name']

        if 'phone' in kwds:
            self.phone = kwds['phone']

        if 'location' in kwds:
            self.location = kwds['location']


    @override
    def __str__(self) -> str:
        return f'name:{self.name}, phone:{self.phone}, location:{self.location}, {super().__str__()}'

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', phone='{self.phone}', location='{self.location}', {super().__repr__()})\n"
    
    @override
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return False

        return str(self) == str(value)
    
    