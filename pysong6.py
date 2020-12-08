me = [1,2,3,4]
you = []


def go_away(lst):
    p = me.pop()
    lst.append(p)
    
    
for i in range(len(me)):
    go_away(you)
    print(i, me, you)