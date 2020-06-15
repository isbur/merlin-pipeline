from merlindiary.commons import SessionControlCenter


SessionControlCenter.init()
assert SessionControlCenter.login().status_code == 200