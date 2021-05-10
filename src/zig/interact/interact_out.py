from typing import Union
from ..element import Element

from .interact_in import InteractIn


class BaseOutput:
    # interface
    def __init__(self):
        self.identity = None
        self.attribute = None
        self.dom_type = None
        self.key = None
        self.value = None


class InteractOut(InteractIn):
    def __init__(
        self,
        output_element: Union[Element, str],
        output_attribute: str = None,
        key: str = None,
    ):

        super().__init__(output_element, output_attribute)
