
class BaseIO(object):
    """
    """

    def __init__(self):
        pass

    def write_description(self, writer):
        raise NotImplemented

    def read_description(self, reader):
        raise NotImplemented

    def feed_api(self):
        raise NotImplemented