def vk_chatbot_unloading(data):
    # Dummy function
    return data


def plaintext(data):
    # Dummy function
    return data


def json_file(data):
    # Dummy function
    return data


import json
# assuming data is a json file
def dictionary_of_lists(data):
    data = json.load(data)
    return data




from tweaks.used_in.data_forms import Проставлен, Проставь
проставлен = Проставлен()
проставь = Проставь()


def marks_on_merlindiary(data):
    for lesson in data:
        pass
        if lesson @ проставлен :
            pass
        else:
            проставь | lesson
    return data