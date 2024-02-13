def test(a):
    if a == 1:
        return None
    elif a == 0:
        return 0

a = 1

print(test(a) is not None)

a = 0

print(test(a) is not None)