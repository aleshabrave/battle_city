class MapException(Exception):
    """Exception for map."""

    def __init__(self, message):
        super(MapException, self).__init__(message)
