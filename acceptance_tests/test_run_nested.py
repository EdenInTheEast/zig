from setup import setup
# add zig as package
setup()


from zig import Zig
from zig.main_components import Graph
from zig.html_components import Div

import pandas as pd
import plotly.express as px



# all default
app = Zig()

div = Div()
div_child = Div()
div_child.add([Div(), Div(), Graph()])
div.add([div_child, Div()])


app.add(div)


if __name__ == "__main__":
    expected = {0: {'type': 'div', 'data': {'content': ''}, 'child': {0: {'type': 'div', 'data': {'content': ''}, 'child': {0: {'type': 'div', 'data': {'content': ''}, 'child': []}, 1: {'type': 'div', 'data': {'content': ''}, 'child': []}, 2: {'type': 'graph', 'data': {}, 'child': []}}}, 1: {'type': 'div', 'data': {'content': ''}, 'child': []}}}}

    result = app.run()

    assert result == expected
