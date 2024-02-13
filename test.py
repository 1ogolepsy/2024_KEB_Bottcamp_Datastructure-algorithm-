def out():
    a = 10
    b = 100

    def inner():
        test = a*b
        print(test)
        return
    inner()
    return

out()