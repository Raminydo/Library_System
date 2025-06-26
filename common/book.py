


from typing import Any, override
from common.model_object import ModelObject



class Book(ModelObject):
    __slots__ = ('_Book__title', '_Book__author', '_Book__publisher', '_Book__publication_year', '_Book__isbn', '_ModelObject__id')

    def __init__(self, title: str, author: str, publisher: str, publication_year: str, isbn: str, id: str | None = None) -> None:
        super().__init__(id)
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.isbn = isbn

    # region title
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, value: str) -> None:
        self.__title: str = value # type: ignore
    #endregion


    # region author
    @property
    def author(self) -> str:
        return self.__author
    
    @author.setter
    def author(self, value: str) -> None:
        self.__author: str = value # type: ignore
    #endregion

    # region publisher
    @property
    def publisher(self) -> str:
        return self.__publisher
    
    @publisher.setter
    def publisher(self, value: str) -> None:
        self.__publisher: str = value # type: ignore
    #endregion


    # region publication_year
    @property
    def publication_year(self) -> str:
        return self.__publication_year
    
    @publication_year.setter
    def publication_year(self, value: str) -> None:
        self.__publication_year: str = value # type: ignore
    #endregion

    # region isbn
    @property
    def isbn(self) -> str:
        return self.__isbn
    
    @isbn.setter
    def isbn(self, value: str) -> None:
        self.__isbn: str = value # type: ignore
    #endregion


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        super().__call__(*args, **kwds)

        if 'title' in kwds:
            self.title = kwds['title']

        if 'author' in kwds:
            self.author = kwds['author']

        if 'publisher' in kwds:
            self.publisher = kwds['publisher']

        if 'publication_year' in kwds:
            self.publication_year = kwds['publication_year']

        if 'isbn' in kwds:
            self.isbn = kwds['isbn']


    @override
    def __str__(self) -> str:
        return f'title:{self.title}, author:{self.author}, publisher:{self.publisher}, publication_year:{self.publication_year}, isbn:{self.isbn}, {super().__str__()}'

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title='{self.title}', author='{self.author}', publisher='{self.publisher}', publication_year='{self.publication_year}', isbn='{self.isbn}', {super().__repr__()})\n"
    