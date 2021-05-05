mport dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# don't configure external here
# most users won't use external css
# configure style on initializtion or separate 
# work with bootstrap

app = zig(bg="red", text="blue", font-size=2, font-style="Roman")

# applies zig main css first, then it overrides with external stylesheet


# accept text or hex
zig.bg_color("red")

zig.text_color("blue")

# font size are all relative to the main font-size
zig.font-size = 2
zig.font-style = "Roman"

# added in order
zig.add_style_sheet = "www.sdfjkjsdklf.com"







def graph():
    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    return fig

# how to set class and id?
# how to add css style?
# provide some necessary styles, and also allow manual edits
# How about flex layout? float?

Title = zig.add_component(Title("Hello World", "Pink", 2.5, id="Header"))
Intro = zig.add_component(Paragraph("Dash: A web application framework for Python.", "Blue", 3.5, className="Intro"))
Graph = zig.add_component(Graph(fig))



in_element = Input("text", value="initial value", mark_in="value") 
In = zig.add(Section(Text("Input:"), in_element))
#insert <br>
zig.line_break(10)


out_element = Text(value="output", id="output" mark_out="value") 
zig.add(Section(Out_element))



interact1 = interact(input=[in_element], output=[out_element])
zig.add_interaction(interact1)



def change_out(input_value): 
    return 'Output: {}'.format(input_value)


def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig



input_slider = Slider()
output_graph = Graph(fig)

zig.add_section(output_graph, input_slider)


interaction = interact(input_slider, output_graph)

# can have more than one chain
interaction.map(update_figure)







# div. what other should we allow nesting?
# table
# ul
#  
Graph = zig.addSection(Section(Title, Intro, Graph))

Section.addChild(Paragraph("Hello Kitty"))

Section.showChildren()


# Allow us to reorganize structure
"""
    Backend will look at all the configurations, and send configuration to Angular app component.
     

"""

zig.render(Intro, Title, Graph)



zig.showTree()






app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
