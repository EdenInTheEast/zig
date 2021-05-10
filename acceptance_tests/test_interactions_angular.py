from setup import setup
# add zig as package
setup()

from zig import Zig
from zig.interact import Interact, InteractIn, InteractOut 
from zig.html_components import *


def test_one():
    app = Zig()

    def return_fn(in_value):
        return in_value
        

    textbox = InputText("initial value", id="123")
    display = Div(id="456")
    frame = Div().add([textbox, display])

    app.add(frame)

    zig_interaction = Interact( InteractIn(textbox),
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

    expected_blueprint = {'sections': {0: {'dom_type': 'div', 'data': {'id': None, 'content': ''}, 'child': {0: {'dom_type': 'input', 'data': {'id': '123', 'value': 'initial value', 'type': 'text'}, 'child': {}}, 1: {'dom_type': 'div', 'data': {'id': '456', 'content': ''}, 'child': {}}}}}, 'interactions': {0: {'input': {0: {'id': '123', 'dom_type': 'input', 'attribute': 'value'}}, 'output': {0: {'id': '456', 'dom_type': 'div', 'attribute': 'content'}}, 'api_point': '/interact/0'}}}

    print(result.blueprint)


    assert result.blueprint == expected_blueprint 

