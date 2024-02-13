def out():
    a = 10
    b = 100

    def inner(*val):
        test = val*b
        print(test)
        val = 100
        test = val*b
        print(test)
        return
    inner(a)
    print(a)
    return

out()