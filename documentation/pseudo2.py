



app = Zig()
app = Zig("name")


#style: use settter to make adjustments
app = Zig(background="red", text="blue", font_size="2px", font_style="Roman")

app.background = "blue"
app.text = "blue"
app.font_size = 2px
app.font_style = "Roman"



#Container
app = Zig();
app = Zig(container="Django");
app = Zig("name", container="Django");




"""Sections
"""
# add one section with section_name
app.add(component)
app.add(component, section_name)
# or this?
app.add((component, section_name))



# add multiple section as list. Will be added in order
app.add([component, component, component])

# this???
app.add([component, component, component], [name, name, name])
#this is better
app.add([(component, name), (component,name), (component, name)])
app.add([(component, name), component, (component, name)])


# app.show_sections(). should display the current order
app.show_sections()


# remove section. accepts index or section_name
app.remove_section(index/name)


# insert at index
app.insert_section(component, index)


# how do we change order?
app.swap_sections(1, 3)




"""
Interactions
"""

input_element = Input("text", value="initial", in_mark="value")
output_element = Text(value="ouput", id="output", out_mark="value")

interaction = interact(input=input_element, output=output_element)

zig.add_interaction(interaction)


def interact(value):
    return "Hi {}".format(value)


interaction.map(interact)






app.add_interaction(Interact(Input(inp.id, "value"), 
                           Output(ouput.id, "content"), 
                           update_ouput_div)
                    )





"""
Rendering
"""
#Rendering. Allows user to render without running server
# what purpose does it serve?
app.render()


#run
# should we just trigger render automatically?
app.run()










