# import pprint as pp
# pp_instance = pp.PrettyPrinter(indent=4, width=20, compact=True)
# pprint = pp_instance.pprint
# from pprint import pprint

class Lesson_list_of_group_:

    def __init__(self, X="foo group name"):
        self.groupCode = self.get_groupCode(X)
        self.innerObject = self.get_all_lessons_of_group(X)
        

    def __contains__(self, argument):
        return argument in self.innerObject
            #     А этим перегрузим оператор __contains__ (in)
    #after all:
    #    compare dates
    #        first column of tables
    #    compare number of students,
    #            present students
    #    their marks
    ####

    def get_groupCode(self, groupName):
        groupDict = {
            "Хорошёво":33,
            "Беляево":39
        }
        return groupDict[groupName]
    

    def get_all_lessons_of_group(self, groupName):

        from bs4 import BeautifulSoup

        from .SessionControlCenter import SessionControlCenter

        SessionControlCenter.init()
        SessionControlCenter.login()
        session = SessionControlCenter.session


        try:
            from .config import custom_sort_order # for test purposes
        except:
            custom_sort_order = None
        page = session.get(
            "http://merlindiary.ru/teacher/lessons/index",
            params = {
                "TeacherLessonsSearch[groupCode]":self.groupCode,
                "sort": "-datetime" if not custom_sort_order else custom_sort_order
            }
        )
        page = BeautifulSoup(page.text, "html.parser")

        lesson_list = []
        lesson_entries = page.select("tr[data-key]")
        for entry in lesson_entries:

            lesson = {}

            lesson_id = entry["data-key"]
            lesson["lesson_id"] = lesson_id

            datetime = entry.select_one("td:nth-child(2)").text
            date, time = datetime.split(" в ")
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

            lesson_list.append(lesson)
            # pprint(lesson)
            # print("#"*40)

        return lesson_list

    



def set(lesson):
    pass