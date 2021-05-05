import pytest 
from zig import Zig, Container, FlaskContainer
from flask import Flask


class TestZig:

    @pytest.fixture
    def test_app(self, mocker):
        mocker.patch('zig.FlaskContainer', spec=True) 
        return Zig()  


    #test zig can be initialized
    def test_flaskapp_initialization(self, test_app):
        assert isinstance(test_app, Zig)
        

    #test app_name is set automatically
    def test_app_name_set_automatically(self, test_app):
        test_name = "__main__" 
        assert test_app.app_name == test_name
        

    #test app_name is set manually
    @pytest.mark.parametrize("app_name", ["test", "123", "$%^#*"])
    def test_app_name_set_automatically(self, app_name):
        test_app = Zig(app_name)
        assert test_app.app_name == app_name


    ###test FlaskContainer is created as default
    def test_flask_container_default(self, test_app):
        assert isinstance(test_app.container, FlaskContainer)
    

    #test Flask container argument will trigger _initiate_container
    def test_passed_Flask_argument(self, mocker, test_app):
        mocker.patch.object(Zig, '_initiate_container')

        container_name = "Flask"
        app_name = "test_app"
        test_app = Zig("test_app", container=container_name)
         
        test_app._initiate_container.assert_called_once_with(container_name, app_name)


    ###test able to pass Container instance
    def test_passed_container(self, mocker, test_app):
        
        mock_container = mocker.Mock(spec=FlaskContainer)
        test_app = Zig(container=mock_container)
         
        assert isinstance(test_app.container, Container)


    #test wrong type is pass as Container
    @pytest.mark.parametrize("container_name", ["test", 123])
    def test_wrong_container(self, container_name, test_app):
        with pytest.raises(TypeError):
            test_app(container=container_name)







        
