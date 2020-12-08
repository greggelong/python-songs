import datetime

def go_walking():
    pass

a = datetime.datetime.now()

if a.hour >0 and a.hour<1:
    go_walking()

else:
    print("hour =", a.hour)
    print("minute =", a.minute)
    print("second =", a.second)
    print("microsecond =", a.microsecond)
    print("month =", a.month)
    print("day =", a.day)
    print("year =", a.year)