import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time :{end-start}")
        return result

    return wrapper
def factorial_for(n):
    resurt = 1
    for i in range(1, n+1):
        resurt *= i
    return resurt

def factorial_func(n):
    '''
    factorial by repetition
    :param n: number(int)
    :return: factorial result(int)
    '''
    if n > 1:
        return n * factorial_func(n-1)
    else:
        return 1


@timer
def combination(n, r, factorial):
    return int(factorial(n) / (factorial(n-r)*factorial(r)))


