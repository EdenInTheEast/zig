from ..element import HtmlElement
from ..defaults import DEFAULT_FIELD_CONTENT


class P(HtmlElement):
    dom_type = "p"
    DEFAULT_FIELD = DEFAULT_FIELD_CONTENT

    def __init__(self, content="", **kwargs):
        super().__init__(self, **kwargs)
        self.content = content

    def render(self):
        return {"content": self.content, "id": self.id}
