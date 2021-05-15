def printNumWords (x):
    if type(x) != str:
        return -1
    else:
        res = len(x.split())
        x = (str(res))
        return x