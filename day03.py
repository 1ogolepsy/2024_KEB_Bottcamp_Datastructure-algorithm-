# import webbrowser
# import time
#
# def is_stack_full():
#     global size, stack, top
#     return top >= size-1
#
# def push(data) :
#     global size, stack, top
#     if is_stack_full():
#         print("stack is full.")
#         return
#     top += 1
#     stack[top] = data
#
# def is_stack_empty():
#     global size, stack, top
#     return top == -1
#
# def pop():
#     global size, stack, top
#     if is_stack_empty():
#         print("stack is empty.")
#         return None
#     data = stack[top]
#     stack[top] = None
#     top -= 1
#     return data
#
# def peek():
#     global size, stack, top
#     if is_stack_empty():
#         print("stack is empty.")
#         return None
#     return stack[top]

def check_bracket(expr: str) -> bool:
   '''
   check bracket in expression.
   :param expr: str
   :return: bool
   '''
    stack = list()
    front = ['(', '{', '[', '<']
    back = [')', '}', ']', '>']

    for char in expr:
        if char in front:
            stack.append(char)
        elif char in back:
            if front[back.index(char)] != stack.pop():
                pass
    if not stack:
    return len(stack) == 0

# size = 20
# stack = [None for _ in range(size)]
# top = -1

if __name__ == "__main__":
    expression = input("Input expression : ")
    print(expression, '==>', check_bracket(expression))
