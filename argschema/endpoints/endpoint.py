import argparse


class Endpoint(object):

    def __init__(self, fn, *arg_adders):
        self.fn = fn
        self.arg_adders = arg_adders

    def build_parser(self, parser_kwargs):
        parser = argparse.ArgumentParser(**parser_kwargs)
        for arg_adder in self.arg_adders:
            arg_adder(parser)

        return parser