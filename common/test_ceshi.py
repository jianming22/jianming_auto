import time
import logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def setup_module():
    # print("\n每个模块前都执行一次")
    logging.info("准备测试数据")
    time.sleep(1)
def teardown_module():
    # print("每个模块后都执行一次")
    logging.info("清理数据")
    time.sleep(1)


def test_xinjian():
    # print("新建用户")
    logging.info("新建用户成功")
    time.sleep(1)


def test_xiugai():
    a = "1"
    assert a == "1"
    # print("修改用户信息")
    logging.info("修改用户成功")
    time.sleep(1)
def test_del():
    # print("删除用户")
    logging.info("删除用户成功")
    time.sleep(1)

