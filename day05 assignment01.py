def ten_to_binaryx (n):
    if n // 2 == 0:
        return str(n %2)
    else:
        result = ten_to_binaryx(n // 2) + str(n % 2)
        return result


def ten_to_oct(n):
    if n // 8 == 0:
        return str(n % 8)
    else:
        result = ten_to_oct(n // 8) + str(n % 8)
        return result


def ten_to_hex(n):
    if n // 16 == 0:
        return str(n % 16)
    else:
        result = ten_to_binaryx(n // 16) + str(n % 16)
        return result

if __name__ == "__main__":
    n = int(input("변환할 수를 입력하세요. : "))
    print(f'2진수 : {ten_to_binaryx(n)}')
    print(f'8진수 : {ten_to_oct(n)}')
    print(f'16진수 : {ten_to_hex(n)}')