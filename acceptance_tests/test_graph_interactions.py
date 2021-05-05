from setup import setup
# add zig as package
setup()


from zig import Zig
from zig.html_components import Div

import pandas as pd
import plotly.express as px


def test():
    app = Zig()
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    # how does Graph get the initial data from update_graph?
    graph = Graph(id="graph-with-slider")


    slider = Slider(df['year'].min,
                    id = "year-slider", 
                    min = df['year'].min(), 
                    max = df['year'].max(),
                    marks = {str(year): str(year) for year in df['year'].unique()},
                    step =  None
                    )



    def update_graph(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        # important: how to send transition setting to angular?
        fig.update_layout(transition_duration=500)

        return fig 



    app.add(Div(section=[graph, slider]))

    app.add_interaction(Interact(Input(slider.id, "value"),
                                 Output(graph.id, 'figure'),
                                 update_graph
                        ))
    
    

if __name__ == "__main__":
    test()


































