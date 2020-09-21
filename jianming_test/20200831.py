aa = {
    "test1": "111111",
    "test2": "222222",
    "test3": "333333",
    "test4": "444444",
    "test5": "555555",
    "test6": "666666"
}
for i in aa.items():
    bb = {
        "username": i[0],
        "password": i[1]
    }
    print(bb)
