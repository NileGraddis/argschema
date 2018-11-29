

class EndpointSpec(object):

    __slots__ = ['endpoints']

    def __init__(self, **endpoints):
        self.endpoints = endpoints

    
    def add(self, key, endpoint):
        self.endpoints[key] = endpoint


    def keys(self):
        return list(self.endpoints.keys())


    def build(self, parser_kwargs=None):
        if parser_kwargs is None:
            parser_kwargs = {'add_help': False}

        callbacks = {}
        parsers = {}
        for key, endpoint in self.endpoints.items():
            parsers[key] = endpoint.build_parser(parser_kwargs=parser_kwargs)
            callbacks[key] = endpoint.fn

        return parsers, callbacks