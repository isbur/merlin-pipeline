from config import Horoshyovo

from merlindiary.definitions import Lesson_list_of_group_
lesson_list = Lesson_list_of_group_(Horoshyovo)
from merlindiary import definitions as merlindiary




def check(lesson):
    return lesson in lesson_list


def проставь(lesson):
    merlindiary.set(lesson)

