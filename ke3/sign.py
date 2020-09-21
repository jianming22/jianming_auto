import hashlib

def sign(body, key = "12345678"):
    a = body.items()

    b = ["".join(i) for i in a if i[1] and i[0] != "sign"]
    b.sort()
    new_str = "".join(b)+key

    m = hashlib.md5()
    m.update(new_str.encode("utf-8"))
    body["sign"] = m.hexdigest()
    return m.hexdigest()
