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
from merlindiary import check
def dictionary_of_lists(data):

    data = json.load(data)

    # Add some tweaks for next stage
    class Customize:
        def __init__(self, lesson):
            self.innerObject = lesson
            self.проставлен = check(lesson)

    for i, lesson in enumerate(data):
        data[i] = Customize(lesson)

    return data


from merlindiary import проставь

def marks_on_merlindiary(data):
    for lesson in data:
        pass
        if lesson . проставлен :
            pass
        else:
            проставь ( lesson )
    return data