from config import Horoshyovo
from .Detect import detect
from .tweaks import type


class BaseLesson: # base object; without "проставлен"

    def __init__(self, protolesson):
        
        #print("#"*40)
        #print(protolesson)

        self.protolesson = protolesson
        self.date = protolesson["date"]
        self.student_ids = [
            get_student_id_by_(key) for key in protolesson["marks"].keys()
        ]

        protolesson_type = detect | protolesson | type

        if protolesson_type == "Human Input":
            self.marks = {
                get_student_id_by_(key):value
                for key, value in protolesson["marks"].items()
            }
        elif protolesson_type == "Merlindiary":
            self.marks = {
                get_student_id_by_(key):' '.join([
                    str(elem) for elem in value.values()
                ])
                for key, value in protolesson["marks"].items()
            }
            self.id = protolesson["lesson_id"]
        else:
            print(protolesson)
            print(protolesson_type)
            raise NotImplementedError("Or maybe implemented? Huh...")


def get_student_id_by_(key):
    Storage = {
        "Хорошёво":{
            "Макарычев Иван  Алекс":1,
            "Ваня":1,
            "Иван":1,
            "Лукьянов Андрей Вячеславович":37,
            "Андрей":37,
            "Шагинов Владимир Евгеньевич":117,
            "Вова":117,
            "Маркевич Артём Сергеевич":118,
            "Артем":118,
            "Артём":118,
            "Агеев  Константин Владимирович":139,
            "Костя":139,

            "Никита": -1, # какой-то непонятно откуда взявшийся перец
            'Шубина Нелли Валерьевна':-2 # и такая же перчиха
        },
        "Беляево":{
            "Борисов  Олег Михайлович":2,
            "Олег":2,
            "Сергеев Артем Дмитриевич":20,
            "Артем":20,
            "Артём":20
        }
    }
    return Storage[Horoshyovo][key]