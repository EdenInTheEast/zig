import pytest
from zig import Zig, Container, FlaskContainer, FlaskConfiguration
from flask import Flask



class TestFlaskContainer:

        @pytest.fixture
        def test_container(self, mocker):
            test_default_dict = { 'app_name':"__main__", 'static_url_path':"/assets", 'static_directory':"assets", 'template_folder':"templates" }


            configuration = mocker.Mock(spec=FlaskConfiguration)

            mocker.patch('zig.FlaskConfiguration.make_initialization_dict', new=lambda: test_default_dict)
            container = FlaskContainer(configuration)

            return container


        #test initialization success
        def test_container_initialization(self, test_container):            
            assert isinstance(test_container, FlaskContainer)
        

        #test initialization fail


        ##test Flask app creation sucess
        def test_flask_app_creation(self, test_container):
            assert isinstance(test_container.app_instance, Flask)

     
        #test initialization processes are called
        def test_flask_initization_processes(self, mocker):
            pass




