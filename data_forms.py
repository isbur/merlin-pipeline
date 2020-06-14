def vk_chatbot_unloading(data):
    # Dummy function
    pass
    return data


def plaintext(data):
    # Dummy function
    # See Data.get()
    pass
    return data


def json_file(data):
    # Dummy function
    # See Data.get()
    pass
    return data


import json
# assuming data is a json file
def dictionary_of_lists(data):
    data = json.load(data)
    return data


from tweaks.merlindiary import *
# But maybe this is unnecessary...
data = transmute(data)  # Some magic happens here!
####
def marks_on_merlindiary(data):
    for lesson in data:
        pass
        if lesson @ проставлен :
            pass
        else:
            проставь | lesson
    return data