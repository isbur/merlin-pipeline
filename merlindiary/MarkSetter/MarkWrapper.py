from .set_marks import Marks


def launch(MarkSetter_instance):

    нужно спасти от перезатирания конфликтующие уроки!

    MarkSetter_instance.set_all()

class MarkSetter(Marks):

    def __init__(self, lesson):

        Marks.__init__(self, lesson.id)

        inputs = open("marks.input", "w")

        s = ""
        for key, value in lesson.marks.item():
            s += key + " " + value
            s += "\n"
        
        inputs.write(s)