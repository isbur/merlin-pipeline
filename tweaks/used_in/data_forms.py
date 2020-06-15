from merlindiary.abstract import check, set


class Проставлен:
    def __rmatmul__(self, lesson):   # aka lefthand_operand
        return check (lesson)


class Проставь:
    def __or__(self, lesson):     # aka righthand_operand
        set (lesson)

