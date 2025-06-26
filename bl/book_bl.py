

from copy import deepcopy
from typing import override
from bl.base_bl import BaseBL
from common.book import Book
from common.data_type import Message, MethodResult, State


class BookBL(BaseBL):

    @override
    def _validation(self, instance: Book) -> MethodResult:
        err_list = []

        if not instance.title:
            err_list.append(Message(field='title', value='title error'))
        
        if (not instance.author):
            err_list.append(Message(field='author', value='author error'))

        if (not instance.publisher):
            err_list.append(Message(field='publisher', value='publisher error'))

        if (not instance.publication_year) or (not instance.publication_year.isdigit()) or (len(instance.publication_year) != 4):
            err_list.append(Message(field='publication_year', value='publication year error'))

        if (not instance.isbn) or (not instance.isbn.isdigit()):
            err_list.append(Message(field='isbn', value='isbn error'))

        for book in self._data_list:
            if (book.id != instance.id) and (book.isbn == instance.isbn):
                err_list.append(Message(field='isbn', value=f'{instance.isbn} exists'))
                break

        if err_list:
            return MethodResult(State.ERROR, *err_list)
        else:
            return MethodResult(State.SUCCESS)
        

    @override
    def _update_instance(self, instance: Book, new_instance: Book):
        instance.title = new_instance.title
        instance.author = new_instance.author
        instance.publisher = new_instance.publisher
        instance.publication_year = new_instance.publication_year
        instance.isbn = new_instance.isbn


    @override
    def _get_file_path(self):
        return r'file/book_list.txt'

