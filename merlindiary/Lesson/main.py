from .BaseLesson import BaseLesson


class Lesson(BaseLesson):

    def __init__(self, protolesson):

        BaseLesson.__init__(self, protolesson)

        from config import Horoshyovo
        from merlindiary.Lesson_list import Lesson_list_of_group_
        lesson_list = Lesson_list_of_group_(Horoshyovo)
        self.проставлен = self in lesson_list

        filtered_lesson_list = [
            lesson for lesson in lesson_list 
            if self.date in [
                lesson.date for lesson in lesson_list
            ]
        ]
        if len(filtered_lesson_list):
            self.exists = True
            self.id = filtered_lesson_list[0].id
        else:
            self.exists = False

