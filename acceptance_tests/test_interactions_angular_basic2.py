from setup import setup
# add zig as package
setup()

from zig import Zig
from zig.interact import Interact, InteractIn, InteractOut 
from zig.html_components import *


def test_one():
    """ Test with 2 basic inputs
    """

    app = Zig()

    def return_fn(in_value, in_value2):
        return in_value + in_value2 
        

    textbox = InputText("initial value", id="123")
    textbox2 = InputText("this too", id="985")
    display = Div(id="456")

    frame = Div().add([textbox, textbox2, display])

    app.add(frame)

    zig_interaction = Interact( [InteractIn(textbox), InteractIn(textbox2)],
                                InteractOut(display),
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

