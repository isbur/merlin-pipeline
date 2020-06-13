from fix import prefix, infix


#Not sure how decorated decorated functions appear in the namespace
#But I have a sense that with direct assignment in conventions.py I can use decorators freely
class customize():

    def __init__(self, instance):
        self.innerObject = instance
    def __rshift__(a, b):
        b.innerObject = a.innerObject


def to_func(a, b):
    return (a, b)
to = infix(to_func)


def transform_func(x):
    (data, function) = x
    data.innerObject = function(data.innerObject)
    return data
transform = prefix(transform_func)

