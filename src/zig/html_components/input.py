from ..element import HtmlElement
from ..defaults import DEFAULT_FIELD_VALUE


class Input(HtmlElement):
    dom_type = "input"
    DEFAULT_FIELD = DEFAULT_FIELD_VALUE

    def __init__(self, value="", **kwargs):
        super().__init__(self, **kwargs)
        self.value = value

    def render(self):
        return {"content": self.content, "id": self.id}
