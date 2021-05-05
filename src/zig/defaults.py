import os


currPath = os.path.dirname(os.path.abspath(__file__))


# Generic container defaults
DEFAULT_TEMPLATE_DIRECTORY = currPath + "/templates"
DEFAULT_ASSETS_DIRECTORY = currPath + "/assets"


# Flask specific defaults
DEFAULT_FLASK_TEMPLATE = "index_flask.html"


# Element specific defaults
DEFAULT_FIELD_CONTENT = "content"
DEFAULT_FIELD_VALUE = "value"


# Section specific defaults
DEFAULT_SECTION_CONFIG = "CoreSection"


# Interact specific defaults
INTERACT_SUBDOMAIN = "interact"
