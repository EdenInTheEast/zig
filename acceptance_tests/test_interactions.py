from setup import setup
# add zig as package
setup()

from zig import Zig
from zig.interact import Interact, InteractIn, InteractOut 
from zig.html_components import Input, Div


def test_one():
    app = Zig()

    def return_fn(in_value):
        return in_value
        

    zig_interaction = Interact( InteractIn(Input(id="123"), "value"),
                                InteractOut(Div(id="456"), "content"),
                                return_fn )

    app.add_interaction(zig_interaction)


    # NOTE: able to run app with interaction alone?
    # what if user forgotten to add element in?
    return app


if __name__ == "__main__":
    app = test_one()

    # will render Interactions 
    # how to test client side and server side interaction?
    result = app.run()

    print(result.blueprint)




