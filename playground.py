import requests
from bs4 import BeautifulSoup

from config import login_page_url


session = requests.Session()
login_page = session.get(login_page_url)
login_page = BeautifulSoup(login_page.text, "html.parser")
test = login_page.select_one("meta[name=csrf-token]")
print(test["content"])