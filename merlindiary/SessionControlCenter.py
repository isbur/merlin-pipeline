import sys

import requests

from config import login_page_url

from .miscellaneous import get_csrf_token_from_


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

        csrf_token = get_csrf_token_from_(login_page)
        
        PostData = {
            "_csrf": csrf_token,
            "LoginForm[username]":"oim177",
            "LoginForm[password]":"merlin010"
        }
        return cls.session.post(login_page_url, PostData)


SessionControlCenter.init()
SessionControlCenter.login()
session = SessionControlCenter.session

