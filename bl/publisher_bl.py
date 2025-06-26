

from copy import deepcopy
from typing import override
from bl.base_bl import BaseBL
from common.publisher import Publisher
from common.data_type import Message, MethodResult, State


class PublisherBL(BaseBL):

    @override
    def _validation(self, instance: Publisher) -> MethodResult:
        err_list = []

        if (not instance.name) or (not instance.name.isalpha):
            err_list.append(Message(field='name', value='name error'))

        if (not instance.phone) or (not instance.phone.isdigit()):
            err_list.append(Message(field='phone', value='phone error'))

        if (not instance.location):
            err_list.append(Message(field='location', value='location error'))

        for publisher in self._data_list:
            if (publisher.id != instance.id) and (publisher.phone == instance.phone):
                err_list.append(Message(field='phone', value=f'{instance.phone} exists'))
                break

        if err_list:
            return MethodResult(State.ERROR, *err_list)
        else:
            return MethodResult(State.SUCCESS)
        

    @override
    def _update_instance(self, instance: Publisher, new_instance: Publisher):
            instance.name = new_instance.name
            instance.phone = new_instance.phone
            instance.location = new_instance.location


    @override
    def _get_file_path(self):
        return r'file/publisher_list.txt'
    
