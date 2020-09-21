import pytest


@pytest.mark.parametrize("test_input,expected",
                         [
                             ({'username': 'admin','password': '123456'},{'code': '1','msg': 'login success!'}),
                             ({'username': 'admin1','password': '111111'},{'code': '102','msg': 'login fail!'}),
                         ]
                         )
def test_log(test_input,expected):
    a = test_input["username"]
    b = test_input["password"]
    c = expected["code"]
    d = expected["msg"]
    print("\n"+a)
    print(b)
    print(c)
    print(d)