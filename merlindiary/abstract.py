from tweaks.used_in.merlindiary.abstract import All, Group, Lessons, Lesson_list
all = All()
group = Group()
lessons = Lessons()
lesson_list = Lesson_list()

from . import concrete
from .concrete.actions import get

from config import Horoshyovo




def check(lesson):
    get (all | Horoshyovo-group | lessons) >> lesson_list
    return lesson in lesson_list


def set(lesson):
    concrete.actions.set(lesson)




