import os
print(os.getcwd())


file = open("merlindiary/config.py", "w")
file.write("sort_order = \"datetime\"")
file.close()


from merlindiary.definitions import Lesson_list_of_group_
from config import Horoshyovo
instance = Lesson_list_of_group_(Horoshyovo)


assert instance.innerObject[0]["date"] == "04/10/2019"