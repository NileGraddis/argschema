
class AddableArg(object):
    
    __slots__ = ('a', 'k')

    def __init__(self, *a, **k):
        self.a = a
        self.k = k

    def __call__(self, parser):
        parser.add_argument(*self.a, **self.k)