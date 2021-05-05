# Zig 

Zig is an open-source Python Webapp Framework for ML, Data Science and analytics applications.
Creates webapp easily using other Python ML-related libraries (Pandas) and Plotly without any frontend knowlegde.

Zig can be configured to use Flask(default), Django or other Python web frameworks, while the frontend is rendered by our Angular Library.

 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/), or pipenv(virtual env) to install Zig.

```bash
pip install zig 

Or with virtual environment,
pipenv install zig


```

## Usage

```python
from zig import Zig
from zig.main_components import Graph
from zig.html_components import *

import pandas as pd
from ploty.express import bar 


app = Zig("app_name")


df = pd.DataFrame({
        "Phone OS": ["IOS", "Android", "IOS", "Android", "IOS", "Android"],
        "Amount": [400, 500, 300, 700, 200, 900],
        "City": ["SF", "NY", "SF", "NY", "SF", "NY"]
   	})

fig = bar(df, x="Phone OS", y="Amount", color="City", barmode="group")

# Zig provides nested sections and introspection of sections
# with reusable components that can be passed around
div = Div().add(P("This is your first graph!"))
div.add(Graph(fig))

# Makes coding webapp clean and simple
app.add(div)


# Starts a local dev server on localhost. Uses Flask as default
app.run()


```

## Contributing
Angular library is on https://github.com/EdenInTheEast/zig-angular 


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) [2021] [kib]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
