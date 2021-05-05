import pytest
import requests


from zig import Zig
from zig.interact import *
from zig.html_components import *


from runner import ClientFlask, LiveFlaskServer 
from runner2 import FlaskThread




class TestInteractionIntegration:
    """
        - runs with dummy client
        - runs with selenium

        - test render response
        - test interaction api point: get
        - test interaction api point: put 

        - test actual interaction


    """

    @pytest.fixture
    def thread_server(self):
        with LiveFlaskServer() as starter:
            yield starter


    @pytest.fixture
    def server(self, thread_server):
        with ClientFlask(thread_server) as cf:
            yield cf


    @pytest.fixture
    def basic_interaction(self):
        app = Zig("test_app")
        
        return_callback = lambda x: x
        
        zig_interaction = Interact( InteractIn(Input(id="234"), "value"),
                                InteractOut(Div(id="345"), "content"),
                                return_callback )

        app.add_interaction(zig_interaction)
        return app


    def test_interaction_render_response(self, basic_interaction, server):
        # use python requests to send get and parse api


        app = basic_interaction
        expected_response = {'interactions': {'0': {'api_point': '/interact/0',
                                                    'input': {'0': {'attribute': 'value', 'dom_type': 'input', 'id': '234'}},
                                                    'output': {'0': {'attribute': 'content', 'dom_type': 'div', 'id': '345'}}}}, 
                                                    "sections":{}}    

        '''
        with client.run(app) as c:
            # client needs to run server in thread
            # then need to send http get request to send
            # and client should return response

            assert c.get('/') == expected_response 
        '''
        #another method
        server.start_server(app) 
        
        #TODO: need to get server index and api point from app object 
        #TODO: a common api parse object?
        response = requests.get("http://127.0.0.1:5000/api")
        
        assert response.status_code == 200
        assert response.headers['content-type'] == 'application/json'
        assert response.json() == expected_response 

        #assert client.get('/') == expected_response


    def test_interaction_render_response_2(self, basic_interaction):
        app = basic_interaction
        expected_response = {}    

        ''' 
        with FlaskThread(app) as thread:
            # client needs to run server in thread
            # then need to send http get request to send
            # and client should return response

            print(thread) 
        '''


    def test_interaction_api_get(self):
        # use a dummy client
        pass


    def test_interaction_api_put(self):
        pass




    def test_browser_interaction_basic(self):
        # use selenium client
        pass











