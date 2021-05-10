from ..element import HtmlElement
from ..defaults import DEFAULT_FIELD_VALUE


class Input(HtmlElement):
    dom_type = "input"
    DEFAULT_FIELD = DEFAULT_FIELD_VALUE

    def __init__(self, value="",**kwargs):
        super().__init__(self, **kwargs)
        self.value = value
        self.input_type = "generic"

    def render(self):
        return {"id": self.id, "value": self.value, }



class InputText(HtmlElement):
    dom_type = "input"
    DEFAULT_FIELD = DEFAULT_FIELD_VALUE

    def __init__(self, value="", **kwargs):
        super().__init__(self, **kwargs)
        self.value = value
        self.input_type = "text"

    def render(self):
        return {"id": self.id, "value": self.value, "type": self.input_type}


