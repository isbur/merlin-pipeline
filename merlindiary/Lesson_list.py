from datetime import datetime
from config import Horoshyovo
from config import start_date
from .Lesson.BaseLesson import BaseLesson as Lesson


class Lesson_list_of_group_:

    def __init__(self, X="foo group name", testmode = False):
        self.groupName = X
        self.groupCode = self.get_groupCode(X)
        self.innerObject = self.get_all_lessons_of_group(X, testmode)
    
    def __contains__(self, lesson_from_input):

        if type(lesson_from_input) == type({}):
            lesson_from_input = Lesson(lesson_from_input)
        if lesson_from_input.__class__.__name__ != "Lesson":
            print("Извините, что вмешиваюсь, но вы подсовываете мне какую-то дичь!")
            print(dir())
            print(__file__)
            print(type(lesson_from_input))

        verdict = any([
            all([
                lesson_from_input.date == lesson_from_merlindiary.date,
                all(
                    ( student_id in lesson_from_merlindiary.student_ids )
                    for student_id in lesson_from_input.student_ids
                ),
                all(
                    ( lesson_from_input.marks[student_id]  == lesson_from_merlindiary.marks[student_id] )
                    for student_id in lesson_from_input.student_ids
                )
            ])
            for lesson_from_merlindiary in self.innerObject
        ])
        return verdict

    def __getitem__(self,key):
        return [
            lesson 
            for lesson in self.innerObject
            if str(lesson.id) == str(key) # str type casting just in case...
        ][0]
    
    def __iter__(self):
        return iter(self.innerObject)

    def __str__(self):
        return self.innerObject.__str__()

    def get_groupCode(self, groupName):

        from .const_data import mapping_groupName_groupCode

        return mapping_groupName_groupCode[groupName]
    

    def get_all_lessons_of_group(self, groupName, testmode=False):

        from bs4 import BeautifulSoup
        from .SessionControlCenter import session

        if testmode:
            from .config import custom_sort_order
        else:
            custom_sort_order = None
        page = session.get(
            "http://merlindiary.ru/teacher/lessons/index",
            params = {
                "TeacherLessonsSearch[groupCode]":self.groupCode,
                "sort": "-datetime" if not testmode else custom_sort_order
            }
        )
        page = BeautifulSoup(page.text, "html.parser")

        lesson_list = []
        lesson_entries = page.select("tr[data-key]")
        for entry in lesson_entries:

            lesson = {}

            lesson_id = entry["data-key"]
            lesson["lesson_id"] = lesson_id

            datetime_string = entry.select_one("td:nth-child(2)").text
            date, time = datetime_string.split(" в ")
            lesson["date"] = date
            lesson["time"] = time

            lesson_page = session.get(
                "http://merlindiary.ru/teacher/students-in-lesson",
                params = {
                    "id":lesson_id
                }
            )
            lesson_page = BeautifulSoup(lesson_page.text, "html.parser")

            marks = {}
            mark_entries = lesson_page.select("tr[data-key]")
            for row in mark_entries:
                fullname = row.select_one("td:nth-child(2)").text
                marks_of_a_student = {
                    "mark_work_at_lesson" : row.select_one("div[id*='mark_work_at_lesson']>div.kv-editable-value").text,
                    "mark_homework" : row.select_one("div[id*='mark_homework']>div.kv-editable-value").text,
                    "mark_dictation" : row.select_one("div[id*='mark_dictation']>div.kv-editable-value").text
                }
                marks[fullname] = marks_of_a_student
            lesson["marks"] = marks


            if  datetime.strptime(
                lesson["date"], "%d/%m/%Y"
            ) < start_date:
                break
                # There are some trashy lessons with mixup of both groups O_o
                # Were they splitted? Hm...

            lesson_list.append(Lesson(lesson))

            if testmode:
                break

        return lesson_list
    
    def update(self):
        self.innerObject = self.get_all_lessons_of_group(
            self.groupName
        )


lesson_list = Lesson_list_of_group_(Horoshyovo)

