from operator import add

def curry(f):
    """
    >>> curry(add)(2)(3)
    5
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


