def fibonacci(n):
    global count, fibonacci_arr
    count += 1

    if fibonacci_arr[n] != None:
        return fibonacci_arr[n]
    else:
        fibonacci_arr[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibonacci_arr[n]

count = 0
fibonacci_arr = [0,1] + [None for _ in range(100)]

n = int(input("계산할 피보나치 수열의 index : "))
fibonacci(n)
print(fibonacci_arr)
print(count)

