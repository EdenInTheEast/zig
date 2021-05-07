from typing import Callable, Any

from flask import Flask, Blueprint, request, render_template, make_response

from .config import ContainerConfiguration, FlaskConfiguration
from .interact import Interact
from .defaults import INTERACT_SUBDOMAIN
from .exceptions import UpdateRouteException


class Container:
    """
    abstract class that allows us to plug in Flask or even other server Framework.
    Decouples from Flask

    """

    def __init__(self, container_configuration: ContainerConfiguration):
        """
        Different types of Container might have different initization procedures,
        and should implement their own initialization methods.

        """
        self.config = container_configuration

    def _initialize(self):
        pass

    def set_index_view(self):
        pass

    def add_api_end_point(self):
        pass

    def run(self):
        pass


class FlaskContainer(Container):
    """
    uses Flask as framework

    """

    def __init__(self, container_configuration: FlaskConfiguration):
        super().__init__(container_configuration)

        self.interactions = None

        # initialize procedures
        if not getattr(self, "app_instance", None):
            # add
            self.app_instance = self._initialize(self.config)

    """ initialize methods
    """

    def _initialize(self, container_configuration: FlaskConfiguration) -> Flask:
        # Template method: a series of operations to initialize the app

        app = self._create_app(container_configuration)

        if app:
            if self._create_initial_routes(app):
                return app

        raise Exception("Unable to create app")

    def _create_app(self, container_configuration: FlaskConfiguration):
        try:
            return Flask(**container_configuration.make_initialization_dict())
        except Exception:
            raise SystemError(
                "Unable to create Flask app with configuration: {}".format(
                    container_configuration
                )
            )

    def _create_initial_routes(self, app):
        # a set of operations to start
        # add url routes
        app = self.set_index_view(app, self.config.template_index_name)

        return app

    def set_index_view(
        self,
        app=None,
        index_file_name: str = "",
        index_url: str = "/",
        index_end_point: str = "index",
    ):
        app = app if app else self.app_instance

        app.add_url_rule(
            index_url, index_end_point, lambda: render_template(index_file_name)
        )

        return app


    def add_url_route(self, 
                      app, 
                      url: str,
                      end_point: str,
                      callback: Callable,
                      ):

        app.add_url_rule(url, end_point, callback)

        return app
        


    """ Update methods
    """

    def update_routes(self):
        # NOTE: non-functional, uses self.app_instance and configuration
        app = self.app_instance

        # creates api url for zig blueprint
        if app:
            app = self.add_api_end_point(app, self.config.blueprint)

            # interact-specified process
            if app:
                app = self._interactions_process(app, self.interactions)
                return app

        raise UpdateRouteException("Update process fail.")

    # able to iterate and add.
    # encapsulate so that other container can implement their own methods
    def add_api_end_point(
        self,
        app: Flask,
        api_json: dict,
        api_url: str = "/api",
        api_end_point: str = "api",
    ):
        app.add_url_rule(api_url, api_end_point, lambda: make_response(api_json))

        return app

    """ Blueprint methods
    """

    def _interactions_process(self, app: Flask, interactions):
        # TEMPLATE method for all interaction-related process

        # creates flask blueprint
        flask_blueprint = self._create_flask_blueprint(INTERACT_SUBDOMAIN)

        # add url routes for flask blueprint
        if flask_blueprint:
            for i in interactions.values():
                if isinstance(i, Interact):
                    flask_blueprint = self._add_blueprint_url(
                        flask_blueprint,
                        i.id,
                        i.api_point,
                        i.http_response,
                    )
        else:
            raise Exception("Need Flask Blueprint")

        # register flask blueprint
        app = self._register_flask_blueprint(app, flask_blueprint)
        return app

    def _interaction_http_response(self, callback: Callable):
        # uses Flask request object
        if request:
            response = callback(request.method, request.form)
        else:
            raise Exception("Requires Request object")

        return make_response(response)

    def _create_flask_blueprint(self, blueprint_name: str):
        # NOTE: WHERE SHOULD WE GET BLUEPRINT NAME FROM?
        interaction_blueprint = Blueprint(blueprint_name, __name__)
        return interaction_blueprint

    def _add_blueprint_url(
        self,
        blueprint_app: Blueprint,
        interact_id: str,
        interact_url: str,
        interact_callback: Callable[..., Any],
        blueprint_name_space: str = INTERACT_SUBDOMAIN,
    ):
        # NOTE: Flask api format: need to differentiate this from actual url
        # Flask auto prepend each endpoint with blueprint name
        api_end_point = interact_id
        # NOTE: this needs to be accessible
        methods = ["POST", "GET", "PUT"]

        blueprint_app.add_url_rule(
            interact_url,
            api_end_point,
            self._interaction_http_response,
            defaults={"callback": interact_callback},
            methods=methods,
        )

        return blueprint_app

    def _register_flask_blueprint(self, app, flask_blueprint):

        app.register_blueprint(flask_blueprint)
        return app

    """ Server methods
    """

    def run(self):
        
        """need host/port and other configurations"""
        self.app_instance.run(host=self.config.host, 
                              port=self.config.port)


