def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def push(data) :
    global SIZE, stack, top
    if is_stack_full():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False
def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("스텍이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("스텍이 비었습니다.")
        return None
    return stack[top]

SIZE = int(input("스택의 크기를 입력하세요 ==> "))
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__":

    # while select != 'X' and select != 'x':
    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

        if select == 'X' and select == 'x':
            print("프로그램 종료!")
            break
        if select=='I' or select =='i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)
        elif select=='E' or select =='e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        elif select=='V' or select =='v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        else :
            print("입력이 잘못됨")


