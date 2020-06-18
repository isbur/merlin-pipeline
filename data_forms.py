def vk_chatbot_unloading(data):
    # Dummy function
    return data


def plaintext(data):
    # Dummy function
    return data


def json_file(data):
    # Dummy function
    return data


import json # assuming data is a json file
from merlindiary import Lesson
def list_of_Lesson_objects(data):

    data = json.load(data)
    for i, protolesson in enumerate(data):
        data[i] = Lesson(protolesson)

    return data


from tweaks_used_in.data_forms import проставь

def marks_on_merlindiary(data):
    for lesson in data:
        
        print(lesson)
        
        if lesson . проставлен :
            pass
        else:
            проставь ( lesson )
    return data