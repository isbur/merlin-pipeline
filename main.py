from tweaks_used_in.main import customize,      \
                                transform,      \
                                to
from data_forms import  vk_chatbot_unloading,   \
                        plaintext,              \
                        json_file,              \
                        list_of_Lesson_objects, \
                        marks_on_merlindiary
from config import horoshyovo
file = open("inputs/"+horoshyovo+".json", "r")
file, data = [customize(obj) for obj in [file, ""]]




file >> data
for form_of_data in (
    vk_chatbot_unloading,
    plaintext,
    json_file,
    list_of_Lesson_objects,
    marks_on_merlindiary
):
    transform | data /to/ form_of_data

