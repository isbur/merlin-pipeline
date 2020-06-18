import os
from ..const_data import mapping_studentId_studentName
from .set_marks import Marks


def launch(MarkSetter_instance):

    # нужно спасти от перезатирания конфликтующие уроки!
    # Done;
    # See tweaks_used_in/data_forms.py

    MarkSetter_instance.set_all()


class MarkSetter(Marks):

    def __init__(self, lesson):

        Marks.__init__(self, lesson.id)


        old_dir = os.getcwd()
        os.chdir(
            os.path.dirname(
                os.path.realpath(__file__)
            )
        )

        inputs = open("marks.input", "w")

        s = ""
        for key, value in lesson.marks.items():
            if int(key) < 0:
                continue

            s += mapping_studentId_studentName[key] + " " + value
            s += "\n"

        inputs.write(s)
        inputs.close()

        os.chdir(old_dir)