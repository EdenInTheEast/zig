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

app.add(Div())
app.add(Div(id="123"))
app.add(Div())
app.add(Div())


if __name__ == "__main__":
    result = app.run()

    print(result)

   
