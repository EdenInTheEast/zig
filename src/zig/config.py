from typing import Union

from .defaults import DEFAULT_FLASK_TEMPLATE



class Configuration:
    """use to pass and compile system configuration"""

    def __init__(self):
        pass


class StyleConfiguration(Configuration):
    def __init__(self):
        pass


class InteractConfiguration(Configuration):
    def __init__(self):
        pass


class BasicInteractConfiguration(Configuration):
    def __init__(self):
        pass


class ContainerConfiguration(Configuration):
    """
    Container-agnostic settings to be set at Zig-level.
    Container-specific configuration(e.g Blueprints) will be set at
    in specific ContainerConfiguration
    Different containers will have different argument names

    Purpose of the container is to make container class cleaner by
    consolidating all configurations requirements here.
    """

    def __init__(
        self, 
        app_name, 
        static_url=None, 
        static_directory=None, 
        template_directory=None,
        host=None,
        port=None
    ):
        self.app_name = app_name
        # Zig blue print: dict of all layout and interact elements
        self.blue_print = None

        # server attributes
        self.host = host if host else "127.0.0.1"
        self.port = port if port else 5000


    def make_initialization_dict(self):
        pass


class FlaskConfiguration(ContainerConfiguration):
    def __init__(
        self,
        app_name: str,
        static_url: str,
        static_directory: str,
        template_directory: str,
        template_index_name: str,
        blueprint: dict = None,
        host: str =None,
        port: Union[str, int] =None
    ):
        # parent initialization
        super().__init__(self, app_name, host=host, port=port)

        # flask initialization parameters
        self.import_name = app_name
        self.static_url_path = static_url
        self.static_folder = static_directory
        self.template_folder = template_directory

        self.template_index_name = (
            DEFAULT_FLASK_TEMPLATE
            if template_index_name is None
            else template_index_name
        )

        # pass layout data to Flask. Should be able to configure later
        self.blueprint = blueprint if blueprint else {}


    """
        Return dictionary with the required parameters for Flask app initialization
            - memorize or lazy load?
    """

    def make_initialization_dict(self):
        return {
            "import_name": self.import_name,
            "static_url_path": self.static_url_path,
            "static_folder": self.static_folder,
            "template_folder": self.template_folder,
        }
