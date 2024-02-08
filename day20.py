
def print_poly(f_x) -> str:
    term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]

        if coefficient >= 0:
            poly_expression += "+"
        poly_expression = poly_expression + f"{coefficient}x^{term} "
        term -= 1

    return poly_expression


def calculation_Poly(x_value, f_x):
    return_Value = 0
    term = len(f_x) - 1

    for i in range(len(fx)):
        coefficient = f_x[i]
        return_Value += coefficient * pow(x_value, term)
        term  = term - 1

    return return_Value



fx = [3, 4, 0, -9]

if __name__ == "__main__":
    print(print_poly(fx))

    print(calculation_Poly(int(input("X 값-->")), fx))


