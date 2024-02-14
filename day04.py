
def fibonacci_repetion(n):
    fibonacci_array = [0, 1]
    #
    # print(fibonacci_array[0])
    # print(fibonacci_array[1])
    for i in range(2, int(n) + 2):
        fibonacci_array.append(fibonacci_array[i - 1] + fibonacci_array[i - 2])
        # print(fibonacci_array[i])
    print(fibonacci_array)

n = input("반복할 횟수를 입력하세요 : ")
fibonacci_repetion(n)