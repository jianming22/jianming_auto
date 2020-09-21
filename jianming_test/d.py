import requests
import json

s = requests.Session()
s.verify = False

url = "http://49.235.92.12:9000/api/v1/login"
r = s.get(url)
# print(r.text)
token = r.json()["cfrctoken"]
h = {
    "cfrctoken":token
}
s.headers.update(h)

# body = {
#     "username":"test",
#     "password":"123456"
# }
# r =
