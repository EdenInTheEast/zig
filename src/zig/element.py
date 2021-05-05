from abc import ABC, abstractmethod

from .section import SectionAttacher


class BaseElement(ABC):
    def __init__(self):
        pass


class Element(BaseElement):
    """
    All html components will be a child of Element
    Different element will implement different Attribute classes
    Element is used to control distribute dffierent attributes

    NEED A WAY TO CHECK FOR INVALID ATTRIBUTES

    """

    def __init__(self, *args, id: str = None, **kwargs):
        # *args will fall through all child args, **kwargs, will fall thru all child kwargs

        # zig should keep a log of all id, and check id during registration

        # NEED TO SANITIZE ALL USER INPUTS
        self.id = id


class DomElement(Element, SectionAttacher):
    """
    All html components will be a child of HtmlElement
    Different element will implement different Attribute classes

    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, **kwargs)
        SectionAttacher.__init__(self, **kwargs)


class HtmlElement(Element, SectionAttacher):
    """
    All html components will be a child of HtmlElement
    Different element will implement different Attribute classes

    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, **kwargs)
        SectionAttacher.__init__(self, **kwargs)
