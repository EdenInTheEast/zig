from collections import defaultdict
from typing import Union

from .section import SectionAttacher


from .container import Container, FlaskContainer
from .config import Configuration, ContainerConfiguration, FlaskConfiguration
from .id_registry import IDRegistry
from .interact import Interact

from .defaults import DEFAULT_ASSETS_DIRECTORY, DEFAULT_TEMPLATE_DIRECTORY


"""
    Research notes:
    - consider using Flask Blueprint if need to separate App
    into different components
"""


class BaseZig:
    # Future-proof interface: able to plug diff. zig implementation to external library
    # For further extension, inherit Zig itself
    def __init__():
        pass


class CoreZig(BaseZig):
    def __init__(
        self,
        *args,
        app_name: str = None,
        background: str = "white",
        text: str = "black",
        font_size: int = 1,
        font_style: str = "Roboto",
        title: str = "zig",
        container: str = "Flask",
        static_directory: str = DEFAULT_ASSETS_DIRECTORY,
        static_url: str = "/assets",
        template_directory: str = DEFAULT_TEMPLATE_DIRECTORY,
        template_index_name: str = None,
        host: str = None,
        port: Union[str, int]= None,
        **kwargs
    ):
        """
            TO-DO:
                - arguments need to be properly ordered for easy reference
                - create resources object for easy reference
                - configuration object

        Style-related parameters




        Container-common parameters


        :param static_directory: sets the directory of static files
            can be a local directory, or external directory (AWS)
            [Default] ``assets``

        :param static_url: sets the route for static files
            [Default] ``/assets``


        Container-specific parameters
        :param template_index_name: determine which index file to use for specific container
            [Default] will be determine at container-specific configuration level


        """
        # main style attributes
        self.background = background
        self.text = text
        self.font_size = font_size
        self.font_style = font_style
        self.title = title

        # layout attributes: IMPLEMENT FROM SECTION
        self.sections = []

        # interaction? should be have a separate object?
        self.interactions = {}

        # initilize borg registry at the start of the project
        self.id_registry = IDRegistry()

        # app name is important for directory loading in Flask
        self.app_name = app_name if app_name else "__main__"

        # container setup. Either pass a string or a container instance
        if isinstance(container, Container):
            # should be able to change the configuration of the container
            self.container = container

        # CONTAINER FACTORY
        elif container in ["Flask"]:
            # able to add other containers in the future
            if container == "Flask":
                # where to check argument?
                self.container_config = FlaskConfiguration(
                    self.app_name,
                    static_url,
                    static_directory,
                    template_directory,
                    template_index_name=template_index_name,
                    host=host,
                    port=port
                )

            self.container = self._initiate_container(self.container_config)
        else:
            raise TypeError("Unknown Container Type: {}".format(container))

    def _initiate_container(
        self, container_configuration: ContainerConfiguration
    ) -> Container:

        if isinstance(container_configuration, FlaskConfiguration):
            try:
                app_container = FlaskContainer(container_configuration)

            except Exception:
                raise
            else:
                return app_container

        else:
            raise TypeError(
                "Unknown Configuration Type: {}".format(container_configuration)
            )

    def add_stylesheet(self, url):
        """
        Allows user to add external stylesheet.
        it is compiled in the order of input.

        Accepts a single url string, or a list of url strings
        """

        # what should we use? a custom object? ordered dict?
        # how about in local directory
        # what other ways to add?

        pass

    def show_stylesheets(self):
        # reveal the order of the stylesheets
        # should we use property or method?
        pass

    def add(self, section):
        """
        Main DOM
        Utitlizes the idea of virtual DOM to divide different sections

        Components are compiled in the order of input, and can be manipulated to change order.
        """
        # what should we use? a Tree objects? what are the specifications?

        # sections needs to be ordered, fast retrieval. Maybe use a dictionary
        # should section itself be an object?
        self.sections.append(section)

    def show_sections(self):
        # reveal the order of the components
        return self.sections

    def line_break(self, number_of_breaks=1):
        """
        Simplify the process of inserting a line break component
        """
        # self.add_component(LineBreak(number_of_breaks))
        pass

    """ Interaction-related methods

    """

    def add_interaction(self, interaction):
        """
        Add all the necessary interactions.


        Accepts Interaction Class.

        """
        self.interactions[interaction.id] = interaction

    def show_interactions(self):
        """return current interactions"""
        return self.interactions

    def render_interactions(self, interactions: Configuration) -> dict:
        """need to render interactions"""

        compiled = dict()

        # key records the interaction id
        for i in interactions.keys():
            # Interact object is in charge of handling rendering on its own
            compiled[i] = interactions[i].render()

        return compiled

    """ Rendering-related methods
    """

    def _render(self, sections, interactions):
        # Internal section rendering
        # render as json. don't store in zig
        # use lazy initialization maybe?
        # return { i:x.to_json() for i,x in enumerate(sections) }
        # return sections[0].to_json()

        # return {i: {"type": x.type, "data": x.render() for i, x in enumerate(sections)}
        return {
            "sections": self.render_sections(sections),
            "interactions": self.render_interactions(interactions),
        }

    def render_sections_list(self, sections):
        total = []

        for x in sections:
            if x.section:
                total.append(
                    {
                        "dom_type": x.dom_type,
                        "data": x.render(),
                        "child": self.render_sections_list(x.section),
                    }
                )
            else:
                total.append({"dom_type": x.dom_type, "data": x.render(), "child": []})

        return total

    def render_sections(self, sections):
        # uses dfs to traverse the n-nary structure recursively
        # which then triggers render() for each element
        # NOTE: recursive-limit
        res = dict()

        for i, x in enumerate(sections):
            if x.section:
                res[i] = {
                    "dom_type": x.dom_type,
                    "data": x.render(),
                    "child": self.render_sections(x.section),
                }
            else:
                res[i] = {"dom_type": x.dom_type, "data": x.render(), "child": []}

        return res

    """ Server-related methods
    """

    def wsgi_entry(self):
        #TODO wsgi-friendly entry point which is container agnostic
        pass



    def _run_server(self, container):
        # Internal server start-up
        try:
            self.container.run()
        except Exception:
            raise
        else:
            return True

    def _update_procedures(self, container: Container):
        try:
            # TODO: change interactions to InteractConfig instead
            container.interactions = self.interactions
            container.update_routes()
        except Exception:
            raise
        else:
            return True

    def run(
        self,
        sections: list = None,
        config: ContainerConfiguration = None,
        container: Container = None,
        interactions: Configuration = None,
        host: str = None,
        port: Union[str, int] = None
    ) -> dict:
        """Template method
        Render the template, and start the server

        :param sections: accepts a list of sections to which it will 
        render in the specific order.
        :param config: will need to use configuration to change/set 
        settings for container
        :param container:
        :return: returns Configuration for introspection
        """
        
        # Initialize
        sections = sections if sections else self.sections
        config = config if config else self.container_config
        container = container if container else self.container
        interactions = interactions if interactions else self.interactions

        # triggers rendering process: converts all to dictionary
        # either pick up up arguments or retrieve from self.sections
        config.blueprint = self._render(sections, interactions)
       

        # TODO: need to be able to change configuration at runtime
        # TODO: need to set host and port

        # each container will trigger their own json-converting process
        # use this to add api point for sending initial json
        # also includes any necessary update procedures
        if self._update_procedures(container):
            if host: config.host = host
            if port: confg.port = port
    
            # starts server
            if self._run_server(container):
                # TODO: should be able to not return anything
                # return the actual blueprint
                return config


class Zig(CoreZig, SectionAttacher):
    """main app
    Uses Composite Pattern with multi-inheritance.
    Allows Zig to be made up of modular components, which will allow further extension
    and customization in the future
    """

    def __init__(self, *arg, **kwargs):
        super().__init__(self, *arg, **kwargs)
        SectionAttacher.__init__(self)
