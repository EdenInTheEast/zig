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
    
    expected = {'sections': {0: {'dom_type': 'div', 'data': {'id':None,'content': ''}, 'child': {0: {'dom_type': 'div', 'data': {'id':None, 'content': ''}, 'child': {0: {'dom_type': 'div', 'data': {'id':None, 'content': ''}, 'child': {}}, 1: {'dom_type': 'div', 'data': {'id':None, 'content': ''}, 'child': {}}, 2: {'dom_type': 'graph', 'data': {'id':None}, 'child': {}}}}, 1: {'dom_type': 'div', 'data': {'id':None, 'content': ''}, 'child': {}}}}}, 'interactions':{}}

    result = app.run()
    print(result.blueprint)

    assert result.blueprint == expected
    
