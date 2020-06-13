from tweaks import  customize,           \
                    transform,                  \
                    to
from data_forms import  vk_chatbot_unloading,   \
                        plaintext,              \
                        json_file,              \
                        dictionary_of_lists,    \
                        marks_on_merlindiary


class Test:
    def __init__(self, obj):
        self = obj # should obj be another reference to some instance to be a valid substitution? 


file = open("input-horoshevo.json", "r")
data = ""
#file, data = [customize(obj) for obj in [file, data]]
print(data)
print(type(data))
print(dir(data))

# Модифицировать базовый мета-класс? Как ограничить scope?
# Создать кастомный мета-класс на основе базового
# Добавить оператор "правого присваивания"
# объектам file и data назначить новый мета-класс
#file >> data
for form_of_data in (
    vk_chatbot_unloading,
    plaintext,
    json_file,
    dictionary_of_lists,
    marks_on_merlindiary
):
    transform | data /to/ form_of_data