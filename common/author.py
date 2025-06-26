


from typing import override, Any
from common.model_object import ModelObject


class Author(ModelObject):
    __slots__ = ('_Author__firstname', '_Author__lastname', '_Author__nationalcode', '_Author__phone', '_ModelObject__id')

    def __init__(self, firstname: str, lastname: str, nationalcode: str, phone: str, id: str | None = None) -> None:
        super().__init__(id=id)
        self.firstname = firstname
        self.lastname = lastname
        self.nationalcode = nationalcode
        self.phone = phone

    # region firstname
    @property
    def firstname(self) -> str:
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        self.__firstname: str = value # type: ignore
    #endregion

    # region lastname
    @property
    def lastname(self) -> str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        self.__lastname: str = value # type: ignore
    #endregion

    # region national code
    @property
    def nationalcode(self) -> str:
        return self.__nationalcode
    
    @nationalcode.setter
    def nationalcode(self, value: str) -> None:
        self.__nationalcode: str = value # type: ignore
    #endregion

    # region phone
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, value: str) -> None:
        self.__phone: str = value # type: ignore
    #endregion

    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        super().__call__(*args, **kwds)

        if 'firstname' in kwds:
            self.firstname = kwds['firstname']

        if 'lastname' in kwds:
            self.lastname = kwds['lastname']

        if 'nationalcode' in kwds:
            self.nationalcode = kwds['nationalcode']

        if 'phone' in kwds:
            self.phone = kwds['phone']


    @override
    def __str__(self) -> str:
        return f'firstname:{self.firstname}, lastname:{self.lastname}, nationalcode:{self.nationalcode}, phone:{self.phone}, {super().__str__()}'

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firstname='{self.firstname}', lastname='{self.lastname}', nationalcode='{self.nationalcode}', phone='{self.phone}', {super().__repr__()})\n"
    