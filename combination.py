
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def combination(n, r):
    return factorial(n) / (factorial(n-r)*factorial(r))



if __name__ == "__main__":
    n = int(input("input n : "))
    r = int(input("input r : "))
    print(f"result {combination(n, r)}")
