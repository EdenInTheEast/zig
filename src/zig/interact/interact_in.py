from typing import Union
from ..element import Element


class BaseInput:
    # interface
    # Interact_In should be in charge of making sure
    # that id, attribute and value are ready to be used
    def __init__(self):
        # the actual object
        self.element = None

        # id
        self.identity = None

        # attribute
        self.attribute = None

        # current value: get this value from element's attribute
        self.value = None

    def get_value(self):
        # get value from input element
        pass


class InteractIn(BaseInput):
    """InteractIn should be in charge of making sure
    that id, attribute and value are ready to be used

    Will auto infer input id and attribute

    Default behavior: without specifiying id and attribute
    :Example:
        # will infer it as div.input, and div.innerhtml
        Input("123")
        Input(Div(id="123"))

        # without id. it will auto-generate id for that element
        Input(Div())

        # with custom attribute
        Input(Div(), "value")


    :param input_element: takes either an Element or string.
                          string should be the id of an existing Element
                          This element will be the target element of input changes

    """

    def __init__(
        self, input_element: Union[Element, str], input_attribute: str, key: str = None
    ):
        # automatically infer input
        self.identity = None
        self.attribute = None
        self.value = None
        self.dom_type = None
        self.key = None

        if isinstance(input_element, Element):
            if input_element.id:
                self.identity = input_element.id
                self.element = input_element
            else:
                # TODO: auto-generate id
                """
                self.identity = input_element.generate_id()
                """

                self.element = input_element

        elif isinstance(input_element, str):
            # TODO: get object from ID registry

            """
            if ID_REGISTERY(input_element):
                self.input_element = ID_REGISTERY(input_element)
                self.identity = self.input_element.id
            """
            pass

        if self.element:
            # don't need to raise if no type.
            self.dom_type = self.element.dom_type

        # TODO: check if it is valid html attribute
        if input_attribute:
            self.attribute = input_attribute
        else:
            # get default field
            self.attribute = self.element.DEFAULT_FIELD

        # NOTE: value is the value of the specified attribute field
        if self.element and self.attribute:
            if hasattr(self.element, self.attribute):
                self.value = getattr(self.element, self.attribute)

    def render(self):
        return {type: self.type, id: self.identity, attribute: self.attribute}
