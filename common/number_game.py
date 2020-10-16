import re
import random
import sys

while True:
    number = random.randint(0, 100)
    a = input("请输入您的数字：")

    if re.match(r'^[0-9_]{1,2}$', a):
        b = int(a)
        if b > number:
            print("您输入的数字%s大于幸运数字%s" % (b, number))
            sys.exit()
        elif b < number:
            print("您输入的数字%s小于幸运数字%s" % (b, number))
            sys.exit()
        else:
            print("您输入的数字%s等于幸运数字%s" % (b, number))
            sys.exit()

    else:
        print("您的输入有误，请重新输入1-2位数字：")
