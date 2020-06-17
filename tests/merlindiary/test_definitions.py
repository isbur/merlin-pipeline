import os


file = open("merlindiary/config.py", "w")
file.write("custom_sort_order = \"datetime\"")
file.close()


from merlindiary.definitions import Lesson_list_of_group_
from config import Horoshyovo
instance = Lesson_list_of_group_(Horoshyovo, testmode = True)


assert instance.innerObject[0]["date"] == "04/10/2019"




test_lesson = {
    "date": "04.10.2019",
    "marks": {
        "Олег": "4 б/0 б/0",
        "Артём": "5 б/0 б/0"
    }
}


print(test_lesson in instance)
assert (test_lesson in instance) == True
