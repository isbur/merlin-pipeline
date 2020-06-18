from config import Horoshyovo
from merlindiary.SessionControlCenter import session
from merlindiary.miscellaneous import get_csrf_token_from_
from .Lesson_list import lesson_list


# We are already sure there is no such lesson
def create(lesson):

    lesson_creation_page = session.get("http://merlindiary.ru/teacher/lessons/create")
    csrf_token = get_csrf_token_from_(lesson_creation_page)

    date  = lesson.date.strftime("%Y-%m-%d")
    

    from .const_data import mapping_groupName_Time
    time = mapping_groupName_Time[Horoshyovo]
    
    from .const_data import mapping_groupName_groupCode
    groupCode = mapping_groupName_groupCode[Horoshyovo]

    session.post(
        "http://merlindiary.ru/teacher/lessons/create",
        data = {
            "_csrf":csrf_token,
            "Lessons[datetime]":date+"+"+time,
            "Lessons[theme]":"auto",
            "Lessons[group_id]": groupCode,
            "Lessons[comment]":""
        }
    )

    lesson_list.update()


    filtered_lesson_list = [
        l
        for l in lesson_list
        if l.date == lesson.date
    ]
    # print("#"*200)

    # print([
    #     e.date for e in lesson_list
    # ])
    # print()



    # #print(filtered_lesson_list)
    # print(lesson)
    # [
    #     print(l.date)
    #     for l
    #     in filtered_lesson_list
    # ]

    if len(filtered_lesson_list) == 1:
        lesson.id = filtered_lesson_list[0].id
        lesson.exists = True
    else:
        raise Exception("Something is strange...")