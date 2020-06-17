from merlindiary.SessionControlCenter import session
from merlindiary.miscellaneous import get_csrf_token_from_


# We are already sure there is no such lesson
def create(lesson):

    lesson_creation_page = session.get("http://merlindiary.ru/teacher/lessons/create")
    csrf_token = get_csrf_token_from_(lesson_creation_page)

    session.post(
        "http://merlindiary.ru/teacher/lessons/create",
        data = {
            "_csrf":csrf_token,
            "Lessons[datetime]":date+"+"+time,
            "Lessons[group_id]": groupCode,
            "Lessons[comment]"	
        }
    )

    lesson.id = ...