""" Container Exceptions
"""


class UpdateRouteException(Exception):
    # Raise when update route fails
    pass


""" ID Exceptions
"""


class IDNotExistException(Exception):
    # Raise when ID does not exist in ID registry
    pass


class IDExistException(Exception):
    # Raise when ID already exists
    pass
