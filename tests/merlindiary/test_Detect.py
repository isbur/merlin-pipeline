from schema import Schema
import pytest


protolesson = {
    "date":"01.01.1991",
    "marks":{
        "Harry":"Potter"
    }
}


s = Schema({
    "date":str,
    "marks":{
        str:str
    }
})

a = s.validate(protolesson)


assert a == protolesson


b = {
    "date":"01.01.1991",
    "marks":{
        "Harry":{
            "Зельеварение":"1"
        }
    }
}

with pytest.raises(Exception):
    assert s.validate(b)


from merlindiary.Lesson.Detect import detect
a = {'date': '06.06.2020', 'marks': {'Андрей': '4 4 4', 'Костя': '3 4 3', 'Артём': '4 3 3'}, 'notes': ['Последнее занятие', 'final'], 'comments': {'Андрей': 'Ожидаемые баллы ОГЭ: 17-22', 'Костя': 'Ожидаемые баллы ОГЭ: 25-29', 'Артём': 'Ожидаемые баллы ОГЭ: 26-29'}}
assert detect(a) == "Human Input"


a = {'date': '<09.05.2020', 'marks': {'Артём': '5 5 4', 'Ваня'
: '3 3 2', 'Никита': '3 3 2', 'Андрей': '3 3 3', 'Костя': 
'3 3 2'}}
# were troubles with missing keys other than "date" and "marks"
assert detect(a) == "Human Input"

