class All:
    def __or__(self, righthand_operand):
        self.innerObject = righthand_operand

class Group:
    def __rsub__(self, lefthand_operand):
        pass

class Lessons:
    def __ror__(self, lefthand_operand):
        pass

class Lesson_list:
    def __rrshift__(self, lefthand_operand):
        self.innerObject = lefthand_operand
    def __contains__(self, argument):
        return argument in self.innerObject