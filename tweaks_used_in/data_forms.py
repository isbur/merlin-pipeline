from LessonCreator import create
from MarkSetter import launch, MarkSetter


# Необходимо, чтобы был определён lesson.id
def проставь(lesson):
    if lesson . exists:
        pass
    else:
        create (lesson)
    # здесь должен быть тест на добавление айди к объекту лессон
    launch( MarkSetter(lesson) )