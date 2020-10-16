import time
def setup_module():
    print("\n每个模块前都执行一次")
    time.sleep(2)
def teardown_module():
    print("每个模块后都执行一次")
    time.sleep(2)


def test_xinjian():
    print("新建用户")
    time.sleep(2)

def test_xiugai():
    a = "1"
    assert a == "1"
    print("修改用户信息")
    time.sleep(2)
def test_del():
    print("删除用户")
    time.sleep(2)

