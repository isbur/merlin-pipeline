from bs4 import BeautifulSoup


"""
Assuming page is result from requests.get()
"""
def get_csrf_token_from_(page):
    
    page = BeautifulSoup(page.text, "html.parser")
    meta_element = page.select_one("meta[name=csrf-token]")
    csrf_token = meta_element["content"]
    return csrf_token