from datetime import datetime
from config import Horoshyovo
from .Detect import detect
from .tweaks import type


class BaseLesson: # base object; without "проставлен"

    def __init__(self, protolesson):

        self.protolesson = protolesson
        self.protolesson["marks"] = {
            key:value
            for key, value
            in self.protolesson["marks"].items()
            if int(get_student_id_by_(key)) >= 0
        }
        self.student_ids = [
            get_student_id_by_(key) 
            for key 
            in protolesson["marks"].keys()
        ]

        protolesson_type = detect | protolesson | type

        if protolesson_type == "Human Input":
            self.date = datetime.strptime(
                protolesson["date"],
                "%d.%m.%Y"
            )
            self.marks = {
                get_student_id_by_(key):value
                for key, value 
                in protolesson["marks"].items()
            }
        elif protolesson_type == "Merlindiary":
            self.date = datetime.strptime(
                protolesson["date"],
                "%d/%m/%Y"
            )
            self.marks = {
                get_student_id_by_(key):' '.join([
                    str(elem) for elem in value.values()
                ])
                for key, value in protolesson["marks"].items()
            }
            self.id = protolesson["lesson_id"]
        else:
            raise NotImplementedError("Or maybe implemented? Huh...")

    def __str__(self):
        return self.__dict__.__str__()
    
    def __repr__(self):
        return self.__dict__.__repr__()

def get_student_id_by_(key):

    from ..const_data import mapping_studentKey_studentId

    return mapping_studentKey_studentId[Horoshyovo][key]