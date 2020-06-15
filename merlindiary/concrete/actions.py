from bs4 import BeautifulSoup
import pandas

from .SessionControlCenter import SessionControlCenter


SessionControlCenter.init()
SessionControlCenter.login()
session = SessionControlCenter.session

def get( all_horoshyovo_group_lessons_strange_object ):

    groupCode = extract
    
    page = session.get(
        "http://merlindiary.ru/teacher/lessons/index",
        params = {
            "TeacherLessonsSearch[groupCode]":groupCode,
            "sort":"-datetime"
        }
    )
    page = BeautifulSoup(page.text, "html.parser")


    tables = pandas.read_html(
        page,
        match = "tr[data-key]"
    )
    print(tables)
    # get all lessons on page?
    # get all lessons on every page?
    # get all lessons starting from specific date?
        # send related data via special object?

    #in particular, you need to:
    #    find on page all tables with attribute "data-key"
    #    filter those with unwanted group value
    
    #if necessary:
    #    get more pages,
    #    extract more lessons


def set(lesson):
    pass
