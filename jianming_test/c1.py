


while 1:
    a = input("请输入您的邮箱账号：")
    b = a[::-1]
    if a[0].isalnum() == True and b[0:4] == "moc." and b[4].isalnum() == True and "@" in b:
        print("欢迎使用")
        break
    else:
        print("邮箱账号格式错误")





