from merlindiary.Lesson_list import lesson_list
from merlindiary.LessonCreator import create
from merlindiary.MarkSetter import launch, MarkSetter


# Необходимо, чтобы был определён lesson.id
def проставь(lesson):
    print(lesson)

    print("#"*40)
    print("Setting marks...\n")
    if lesson . exists:
        if any([
            "б/о б/о б/о" != value
            for key, value 
            in lesson_list[lesson.id].marks.items()
        ]):

            print(lesson_list[lesson.id].marks)

            print("There are some marks already\n")

            print("lesson_id:")
            print(lesson.id)
            print()
            
            return
    else:
        create (lesson)
        print("Created lesson\n")

    launch( MarkSetter(lesson) )
    print("Marks set\n")

    print("lesson_id:")
    print(lesson.id)
    print()