

from abc import ABC, abstractmethod
from copy import deepcopy
from common.author import Author
from common.data_type import Message, MethodResult, State
from common.model_object import ModelObject
from dal.file_manager import FileManager
from common.author import Author
from common.publisher import Publisher
from common.book import Book



class BaseBL(ABC):

    def __init__(self) -> None:
        self.__dal_class = FileManager(path=self._get_file_path())

        result: MethodResult = self.__dal_class.load_data()

        if result.state == State.ERROR:
            raise Exception

        self._data_list: list[ModelObject] = []

        for line in result.return_data:
            self._data_list.append(eval(line.strip()))


    @abstractmethod
    def _get_file_path(self) -> str:
        pass


    @abstractmethod
    def _validation(self):
        return MethodResult(state=State.SUCCESS)


    @abstractmethod
    def _update_instance(self, instance: ModelObject, new_instance: ModelObject):
        pass


    def get_all(self) -> list[ModelObject]:
        return self._data_list
    


    def create(self, instance: ModelObject) -> MethodResult:
        result = self._validation(instance=instance)

        if result.state == State.ERROR:
            return MethodResult(State.ERROR, *result.message)

        result: MethodResult = self.__dal_class.save(instance=instance)

        if result.state == State.ERROR:
            return MethodResult(State.ERROR, Message(field='error', value='error message'))

        self._data_list.append(instance)
        return MethodResult(State.SUCCESS, Message(field='success', value='success message'))



    def delete(self, instance: ModelObject) -> MethodResult:

        selected_index = self._data_list.index(instance)
        self._data_list.remove(instance)
        result: MethodResult = self.__dal_class.save_data(self._data_list, mode='w')

        if result.state == State.ERROR:
            self._data_list.insert(selected_index, instance)

            return MethodResult(State.ERROR, Message(field='error', value='error message'))

        return MethodResult(State.SUCCESS, Message(field='success', value='success message'))



    def update(self, instance: ModelObject) -> MethodResult:
        result = self._validation(instance)

        if result.state == State.ERROR:
            return MethodResult(State.ERROR, *result.message)

        selected_index: int = self._data_list.index(instance)
        selected_instance: ModelObject = self._data_list[selected_index]
        copy_instance: ModelObject = deepcopy(selected_instance)

        self._update_instance(instance=selected_instance, new_instance=instance)

        result: MethodResult = self.__dal_class.save_data(self._data_list, mode='w')

        if result.state == State.ERROR:
            self._update_instance(instance=selected_instance, new_instance=copy_instance)
        
            return MethodResult(State.ERROR, Message(field='error', value='error message'))
    
        
        return MethodResult(State.SUCCESS, Message(field='success', value='success message'))
