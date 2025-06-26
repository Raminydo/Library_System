

from genericpath import isfile
from typing import Literal
from common.book import Book
from common.data_type import MethodResult, State



class FileManager:
    def __init__(self, path: str) -> None:
        self.__path: str = path

    def save(self, instance: Book, mode: Literal['w'] | Literal['a'] = 'a') -> MethodResult:
        file_object = None

        try:
            file_object = open(file=self.__path, mode=mode)
            file_object.write(repr(instance))
        except BaseException as err:
            return MethodResult(state=State.ERROR, return_data=err)
        else:
            return MethodResult(state=State.SUCCESS)
        finally:
            if file_object and (not file_object.closed):
                file_object.close()

    def save_data(self, instance_list: list[Book], mode: Literal['w'] | Literal['a'] = 'a') -> MethodResult:
        file_object = None

        try:
            file_object = open(file=self.__path, mode=mode)
            file_object.writelines(map(lambda instance: repr(instance), instance_list))
        except BaseException as err:
            return MethodResult(state=State.ERROR, return_data=err)
        else:
            return MethodResult(state=State.SUCCESS)
        finally:
            if file_object and (not file_object.closed):
                file_object.close()


    def load_data(self) -> MethodResult:
        file_object = None

        if not isfile(self.__path):
            try:
                file_object = open(file=self.__path, mode='"x"')
            except BaseException as err:
                return MethodResult(state=State.ERROR, return_data=err)
            else:
                return MethodResult(state=State.SUCCESS, return_data=[])
            finally:
                if file_object and (not file_object.closed):
                    file_object.close()

        try:
            file_object = open(file=self.__path)
            res: list[str] = file_object.readlines()
        except BaseException as err:
            return MethodResult(state=State.ERROR, return_data=err)
        else:
            return MethodResult(state=State.SUCCESS, return_data=res)
        finally:
            if file_object and (not file_object.closed):
                file_object.close()


