from setup import setup
# add zig as package
setup()


from zig import Zig
from zig.html_components import Div



def version_one():
    app = Zig()


    section = Div()
    header = H6("Title!")
    output = Div(id="my-output")

    section2 = Div("Input :" )
    inp = Input_text("initial_value", id="my-input")
    section2.add(inp)

    # wrap everything in div
    section.add([header, section2, LINE_BREAK, ouput])

    app.add(section)


    def update_ouput_div(input_value):
        return "Output: {}".format(input_value)



    interaction = Interact(Input(inp.id, "value"), 
                           Output(ouput.id, "content"), 
                           update_ouput_div)

    app.add_interaction(interaction)
    



# Can we just add each section in?


def version_two():
    app = Zig()

    section = Div()
    header = H6("Title!")
    output = Div(id="my-output")

    # method 1
    # possible to add siblings too?
    section2 = Div(section=[
                        Input_text("intial_value", id="my-put"),
                        Div("test")
                    ])
    
    # mtd 2
    section2 = Div().add([Input_text("intial_value", id="my-put"), Div("test")]) 


    # wrap everything in div
    section.add([header, section2, LINE_BREAK, ouput])
    app.add(section)



def version_three():
    app = Zig()


    section = Div(section=[
                    H6("Title!"),
                    Div(section=[
                        Input_text("intial_value", id="my-put"),
                        Div("test")
                    ]),
                    LINE_BREAK,
                    Div(id="my-output")
                ])

    
    app.add(section) 


    def update_ouput_div(input_value):
        return "Output: {}".format(input_value)



    # Input uses id by default. use key arg for other attributes
    add_interaction(Interact(Input(inp.id, "value"), 
                           Output(ouput.id, "content"), 
                           update_ouput_div)
                    )




if __name__ == "__main__":
    pass





