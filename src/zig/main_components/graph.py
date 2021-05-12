import json

from ..element import DomElement
from ..section import CoreSection


class GraphInherit(CoreSection, DomElement):
    dom_type = "graph"

    def __init__(self, figure=None, **kwargs):
        super().__init__()
        DomElement.__init__(self, **kwargs)

        self.figure = figure

    def render(self):
        # convert json to dict. so that it will store in dict as dict instead of string
        if self.figure:
            return json.loads(self.figure.to_json())
        else:
            # WHAT SHOULD WE DO IF FIGURE IS EMPTY?
            return {}

    def to_json2(self):
        return dict(
            {
                "data": getattr(self.figure, "data", None),
                "layout": getattr(self.figure, "layout", None),
                "config": getattr(self.figure, "config", None),
                "frames": getattr(self.figure, "frames", None),
            }
        )


class Graph(DomElement):
    dom_type = "graph"

    def __init__(self, figure=None, **kwargs):
        super().__init__(self, **kwargs)

        self.figure = figure

    def render(self):
        json_dict = {"id": self.id}

        if self.figure:
            # convert json to dict. so that it will store in dict as dict
            # instead of string
            figure_dict = json.loads(self.figure.to_json())
            json_dict = {**json_dict, **figure_dict}

        return json_dict
