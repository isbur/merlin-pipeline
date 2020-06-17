
from .SessionControlCenter import session


class MarkSetter:
    
    def __init__(self, lesson):
        self.lesson_object = lesson
        self.lesson_id = lesson.lesson_id # if not?
        self.base_url = "http://merlindiary.ru/teacher/students-in-lesson"
        self.lesson_page = session.get(
            self.base_url,
            params = {
                "id":self.lesson_id
            }
        )
        self.csrf_token
    
    def __call__(self):
        self.set_marks_for_all_students()
    
    def set_marks_for_all_students(self):
        for student in lesson.students:
            self.current_student_index
            set_all_marks_for_a_student()

    def set_all_marks_for_a_student(self):
        [set_one_mark() for mark in student.marks]

    def set_one_mark(self, student_id, attribute_to_edit, mark):

        index_of_student_to_edit = self.current_student_index
        data = {
            "_csrf": self.csrf_token,
            "hasEditable": 1,
            "editableIndex": index_of_student_to_edit,
            "editableKey": json.dumps({
                "lesson_id": self.lesson_id,
                "student_id": student_id
            }, separators=(",", ":")),
            "editableAttribute": attribute_to_edit,
            "StudentsInLesson[" + str(index_of_student_to_edit) + "][" + str(attribute_to_edit) + "]": mark
        }

        return session.post(
            self.base_url,
            params = {
                "id":self.lesson_id
            }, 
            data = data
        )




