x = set(["a","b","c","d"])

def running():
    print("running")


while True:
    print(x)
    if x == set():
        running()
        break
    else:
        x.pop()