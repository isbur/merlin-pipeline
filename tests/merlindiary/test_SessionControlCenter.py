from merlindiary.SessionControlCenter import SessionControlCenter


SessionControlCenter.init()
assert SessionControlCenter.login().status_code == 200