from tweaks import customize
from tweaks.merlindiary import group, lessons

import concrete
from concrete import get

from config import Horoshyovo


def check(lesson):
    lesson_list = customize([])

    get (all | Horoshyovo-group | lessons) >> lesson_list
    return lesson in lesson_list


def set(lesson):
    concrete.set(lesson)