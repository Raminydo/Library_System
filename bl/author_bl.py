

from copy import deepcopy
from typing import override
from bl.base_bl import BaseBL
from common.author import Author
from common.data_type import Message, MethodResult, State


class AuthorBL(BaseBL):
 

    @override
    def _validation(self, instance: Author) -> MethodResult:
        err_list = []

        if (not instance.firstname) or (not instance.firstname.isalpha):
            err_list.append(Message(field='firstname', value='firstname error'))
        
        if (not instance.lastname) or (not instance.firstname.isalpha):
            err_list.append(Message(field='lastname', value='lastname error'))

        if (not instance.nationalcode) or (not instance.nationalcode.isdigit()):
            err_list.append(Message(field='nationalcode', value='nationalcode error'))

        if (not instance.phone) or (not instance.phone.isdigit()):
            err_list.append(Message(field='phone', value='phone error'))

        for author in self._data_list:
            if (author.id != instance.id) and (author.nationalcode == instance.nationalcode):
                err_list.append(Message(field='nationalcode', value=f'{instance.nationalcode} exists'))
                break

        if err_list:
            return MethodResult(State.ERROR, *err_list)
        else:
            return MethodResult(State.SUCCESS)
        
    
    @override
    def _update_instance(self, instance: Author, new_instance: Author):
        instance.firstname = new_instance.firstname
        instance.lastname = new_instance.lastname
        instance.nationalcode = new_instance.nationalcode
        instance.phone = new_instance.phone

    

    @override
    def _get_file_path(self):
        return r'file/author_list.txt'
        

