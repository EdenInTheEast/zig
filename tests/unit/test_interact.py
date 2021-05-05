import pytest


from zig.interact import Interact, InteractOut 
from zig.interact.interact_in import InteractIn
from zig.html_components import *


class TestInteractBlackBox:
    """
        Basic methods: 
            0. Able to create Interact object with specs [IMPT!]

            1. Store all input elements and their specs
            2. Store all output elements and their specs
            3. Store callback function                        
            4. Create API point

            5. Render Interaction as JSON [IMPT!]

        REST methods:
            1. update input value 
            2. generate output value             

            3. Handle GET Request
            4. Handle POST/PUT Request

    """

    @pytest.fixture
    def fixture_normal_parameters(self):
        # SETUP testing parameters for Mock InteractIn and InteractOut
        para_dict = ["id", "value", "attribute", "dom_type"] 

        # input 1: HtmlElement of type Input, value, id='456'
        input1 = ["456", 3, "value", Input().dom_type]
        input1_dict = {i:x for i, x in zip(para_dict, input1)}
    
        # input 2: HtmlElement of type Div, content, id='123'
        input2 = ["123", "test_value", "content", Div().dom_type]
        input2_dict = {i:x for i, x in zip(para_dict, input2)}

        # ouput 3: HtmlElement of type P, content, id='678'
        output = ["678", "", "content", P().dom_type]
        output_dict = {i:x for i, x in zip(para_dict, output)} 

        # just a placeholder
        callback = lambda x, y: x * y 

        # NOTE: Might implement diff. format for diff. subclasses
        expected_api_point = "/interact/{interaction_id}"

        return {"in1":input1_dict, "in2":input2_dict, 
                "out":output_dict, "callback": callback, 
                "api_point": expected_api_point, "parameters":para_dict}
            

    @pytest.fixture
    def fixture_normal_ini(self, mocker, fixture_normal_parameters): 
        # TEST initialization of Interact 

        input1, input2, output, callback, \
        api_point_format, para_dict = fixture_normal_parameters.values() 

        
        mock_input1 = mocker.patch("zig.interact.InteractIn", 
                                    spec=True, 
                                    identity=input1["id"], 
                                    attribute=input1["attribute"], 
                                    value=input1["value"], 
                                    dom_type=input1["dom_type"],
                                    key=None)

        mock_input2 = mocker.Mock(spec=InteractIn, 
                                  identity=input2["id"],
                                  attribute=input2["attribute"], 
                                  value=input2["value"], 
                                  dom_type=input2["dom_type"],
                                  key=None)

        mock_output = mocker.patch("zig.interact.InteractOut", 
                                    spec=True, 
                                    identity=output["id"], 
                                    attribute=output["attribute"], 
                                    value=output["value"], 
                                    dom_type=output["dom_type"])

        interaction = Interact( [mock_input1, mock_input2],
                                mock_output, 
                                callback)

        return interaction

 
    # blackbox: doesn't need to know how inputs are stored
    def test_input_args(self, fixture_normal_ini, fixture_normal_parameters):
        # TEST that all input elements and their specifications are stored,
        # and can be retrieved. CHECK: inputs_args 
        interaction = fixture_normal_ini 
        expected_arguments = [ fixture_normal_parameters["in1"]["value"], fixture_normal_parameters["in2"]["value"] ]

        assert interaction.inputs_args == expected_arguments


    def test_input_keyword_args(self, fixture_normal_ini):
        # TEST that all input elements can be stored along with their keywords
        # and can be retrieved as such. CHECK: inputs_kwargs 
        pass


    def test_output_elements(self, fixture_normal_ini, fixture_normal_parameters):
        # TEST that all output elements and their specs are stored,
        # and can be retrieved. CHECK: output_dict 

        interaction = fixture_normal_ini
        output = fixture_normal_parameters["out"]
        expected_output_data = None

        # NOTE: might implement diff. format for diff. subclass
        expected_output_elements = {output["id"]: {  
                                        "attribute": output["attribute"],
                                        "dom_type": output["dom_type"],
                                        "data": expected_output_data 
                                    } } 
        # it produces an Ordered Dict
        assert dict(interaction.output_dict) == expected_output_elements 


    
    def test_generate_api_point(self, fixture_normal_ini, fixture_normal_parameters):
        # TEST that it will auto-generate a url for api
        # CHECK: api_point 

        api_point_format  = fixture_normal_parameters["api_point"]
        interaction = fixture_normal_ini
        expected_api_point = api_point_format.format(interaction_id=interaction.id)

        assert interaction.api_point == expected_api_point 


    # NOTE: IMPT it combines a few of the previous tests
    def test_rendering(self, fixture_normal_ini, fixture_normal_parameters):
        # given in and out, able to render into dict object (json-like)
        interaction = fixture_normal_ini
        inputs = [fixture_normal_parameters["in1"], fixture_normal_parameters["in2"]]
        output = [fixture_normal_parameters["out"]]

        input_dict = {i:{"id":v["id"] , "dom_type":v["dom_type"], "attribute":v["attribute"]} 
                      for i,v in  enumerate(inputs) }

        output_dict = {i:{"id":v["id"] , "dom_type":v["dom_type"], "attribute":v["attribute"]} 
                      for i,v in enumerate(output) }

        test_generate_api_point = fixture_normal_parameters["api_point"]    \
                                    .format(interaction_id=interaction.id)


        expected_json = {"input": input_dict, "output": output_dict, "api_point": test_generate_api_point}
        
    
        #NOTE: Interact Object will trigger render on each In and Out Object

        assert interaction.render() == expected_json 


    def test_update_single_input(self, fixture_normal_ini, fixture_normal_parameters):
        # TEST update of single input value from input 2
        
        interaction = fixture_normal_ini 

        # input 2: HtmlElement of type Div, content, id='123'
        new_value = "this is a test value" 
        new_input2 = ["123", "content",  new_value, "div"]


        input2_dict = {i:x for i, x in zip(fixture_normal_parameters["parameters"], new_input2)}
    
        expected_input_values = [fixture_normal_parameters["in1"]["value"], new_input2[2]]

        #TODO: this is incomplete. Need a better way to push update
        assert interaction._update_single_input(*new_input2[:3]) is True
        assert interaction.inputs_args == expected_input_values

    
    def test_process_inputs_generate_output(self, fixture_normal_ini, fixture_normal_parameters):
        # NOTE: NEED TO change test
        # TEST that it is able to generate new output value from callback with input values
        interaction = fixture_normal_ini

        expected_output = fixture_normal_parameters["in1"]["value"] * fixture_normal_parameters["in2"]["value"]
        result = interaction._process_inputs()

        assert result == expected_output


    def test_update_output_values(self):
        # TEST output is generated and updated: 
        pass



    def test_update_via_put(self, fixture_normal_ini, fixture_normal_parameters):
        # TEST update of put response
        interaction = fixture_normal_ini 

        # given dictionary response from external source for input 1
        updated_value = "Hello world!" 
        json_response = { 0:{"type":"div" ,"id":"123" , "data":updated_value, "attribute":"content"}}
        expected_args = [fixture_normal_parameters["in1"]["value"], updated_value]

        # api-point will trigger this function
        interaction.put_response(json_response)
        
        assert interaction.__compile_args() == expected_args


    

    















    


