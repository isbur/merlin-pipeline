# coding=utf-8
from .Fix import prefix, infix


#Not sure how decorated decorated functions appear in the namespace
#But I have a sense that with direct assignment in conventions.py I can use decorators freely
class customize():

    def __init__(self, instance):
        self.innerObject = instance
    def __rshift__(a, b):
        b.innerObject = a.innerObject
    def __rrshift__(self, lefthand_operand):
        # если "правильного" класса
        if "Customized" in lefthand_operand.__class__.__name__:
            self.innerObject = lefthand_operand.innerObject
        # а иначе просто положить в innerObject
        else:
            self.innerObject = lefthand_operand


def to_func(a, b):
    return (a, b)
to = infix(to_func)


def transform_func(x):
    (data, function) = x
    data.innerObject = function(data.innerObject)
    return data
transform = prefix(transform_func)

