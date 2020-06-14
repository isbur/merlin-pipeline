__all__ = ["transmute", "проставлен", "проставь"]


from merlindiary.abstract import check, set


def transmute():
    pass


     А этим перегрузим оператор __contains__ (in)
    #after all:
    #    compare dates
    #        first column of tables
    #    compare number of students,
    #            present students
    #    their marks
    ####


class проставлен:
    @staticmethod
    def __rmatmult__(lesson):   # aka lefthand_operand
        check (lesson)
        pass

class проставь:
    @staticmethod
    def __or__(lesson):     # aka righthand_operand
        set (lesson)
        pass


