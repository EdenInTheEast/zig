from ..element import HtmlElement
from ..section import CoreSection


from ..defaults import DEFAULT_FIELD_CONTENT


class DivInherit(CoreSection, HtmlElement):
    dom_type = "div"

    def __init__(self, content="", **kwargs):
        super().__init__()
        HtmlElement.__init__(self, **kwargs)
        # what if i need to pass diff. kwargs to diff. classes?

        self.content = content

    def render(self):
        json_data = {"content": self.content}

        return json_data


class Div(HtmlElement):
    dom_type = "div"

    # this should be implemented in the Value Attribute Class
    DEFAULT_FIELD = DEFAULT_FIELD_CONTENT

    def __init__(self, content="", **kwargs):
        super().__init__(self, **kwargs)
        self.content = content

    # TODO: put this into HTMLValueELement and HTMLContentElement
    def render(self):
        return {"id": self.id, "content": self.content}

    def get_value(self, attr):
        # return current value of a specific attribute
        if hasattr(self, "attr"):
            pass

        return self.attr
