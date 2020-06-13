from copy import deepcopy
from types import MethodType
from fix import prefix, infix


#Not sure how decorated decorated functions appear in the namespace
#But I have a sense that with direct assignment in conventions.py I can use decorators freely
def customize(obj):
    # Not a bound or class method yet
    def custom_init(self, instance):
        self = instance

    CustomizedClass = type(
        "Customized" + obj.__class__.__name__,
        (obj.__class__, ),
        {
            "__init__": custom_init,
            "__rshift__": right_assignment
        }
    )

    obj = CustomizedClass(obj)

    return obj


def right_assignment(a, b):
    b.__init__(a)


def to_func(a, b):
    return (a, b)
to = infix(to_func)


def transform_func(x):
    (data, function) = x
    return function(data)
transform = prefix(transform_func)

