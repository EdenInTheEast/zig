from collections import defaultdict
from typing import TYPE_CHECKING, Any
from .exceptions import IDExistException


if TYPE_CHECKING:
    from .element import Element


class IDRegistry:
    """
    Uses Borg pattern to maintain a single dictionary

    Possible to inherit from dictionary?

    """

    __registry = defaultdict()

    def __init__(self):
        if not IDRegistry.__registry:
            IDRegistry.__registry = self.__dict__
        else:
            self.__dict__ = IDRegistry.__registry

    def store(self, id: str, obj: Any):
        # store the id and object that it references to
        # TODO QUESTION: do we need to store object?
        # can we compress the stored object?

        if not ID_check:
            IDRegistry.__registry[id] = obj

        raise IDExistException("ID already exist")

    def change_id(self, old_id, new_id):
        pass

    def get(self, id) -> Any:
        # return the corresponding object of the given id
        return self.__registry.get(id, None)

    def get_id(self, id):
        # this function will raise IDNotExistException if it doesn't exist
        if ID_check(self, id):
            return self.__registry[id]
        else:
            raise IDNotExistException("ID {input_element} does not exist")

    def ID_check(self, id):
        # Check if ID exists upon initialization and storage
        if self.__registry.get(id, None):
            return True

        return False
