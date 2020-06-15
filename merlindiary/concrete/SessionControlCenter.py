import sys

import requests
from bs4 import BeautifulSoup

from config import login_page_url


class SessionControlCenter:
    
    @classmethod
    def init(cls):
        cls.session = requests.Session()
    
    @classmethod
    def login(cls):
        try:
            login_page = cls.session.get(login_page_url)
        except:
            print("Try to init() first", file=sys.stderr)
            raise

        login_page = BeautifulSoup(login_page.text, "html.parser")
        meta_element = login_page.select_one("meta[name=csrf-token]")
        csrf_token = meta_element["content"]
        
        PostData = {
            "_csrf": csrf_token,
            "LoginForm[username]":"oim177",
            "LoginForm[password]":"merlin010"
        }
        return cls.session.post(login_page_url, PostData)
