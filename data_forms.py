
# https://stackoverflow.com/a/48100440/10216512
import tweaks
#from customized_operators import transform, to
#import customized_operators.transform as transfrom
#import customized_operators.to as to
transfrom = tweaks.transform
to = tweaks.to            


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


def marks_on_merlindiary(data):
    return data