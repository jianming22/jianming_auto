from ke3.sign import sign
import hashlib

def test_lou():
    url = "https://www.baidu.com"

    body = {
        "username" : "test",
        "password": "123456",
        "email": "",
    }
    sign(body)
    print(body)
    assert body["sign"] == "1aca01806e93bb408041965a817666af"

if __name__ == '__main__':
    a = test_lou()
    print(a)