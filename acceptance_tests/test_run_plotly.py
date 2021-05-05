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

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.add(Graph(fig))

app.add(Graph(fig))

app.add(Div())



if __name__ == "__main__":
    
    app.run()
