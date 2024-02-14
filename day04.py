def decimal_to_octal(number: int) -> int:
    """
    deciaml > aoctal number.
    :param number: integer(base =dec)
    :return: stirng(base octal)
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n // 8) + str(n % 8)
    # octal = ''
    # while number > 0:
    #     octal = str(number % 8) + octal
    #     number = number // 8
    # return octal


n = int(input("Input decimal number : "))
print(decimal_to_octal(n))