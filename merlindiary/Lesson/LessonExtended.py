from .BaseLesson import BaseLesson
from ..Lesson_list import lesson_list


class Lesson(BaseLesson):

    def __init__(self, protolesson):

        BaseLesson.__init__(self, protolesson)
        
        self.проставлен = self in lesson_list

        filtered_lesson_list = [
            lesson 
            for lesson 
            in lesson_list 
            if self.date == lesson.date
        ]
        if len(filtered_lesson_list):
            self.exists = True
            self.id = filtered_lesson_list[0].id
        else:
            self.exists = False

