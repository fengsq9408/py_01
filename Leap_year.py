year = int(input("请输入一个年份:"))
if year % 100 == 0:
    if year % 400 == 0:
        print("%d是闰年" % year)
    else:
        print("%d不是闰年" % year)
else:
    if year % 4 == 0:
        print("%d是闰年" % year)
    else:
        print("%d不是闰年" % year)
