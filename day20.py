import mymath
import time

if __name__ == "__main__":
    n = int(input("input n : "))
    r = int(input("input r : "))

    print(f"{mymath.combination(n,r, mymath.factorial_func)}")
