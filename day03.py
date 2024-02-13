import webbrowser
import time

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

SIZE = 3
stack = [ None for _ in range(SIZE) ]
top = -1

if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com', 'inha.ac.kr']

    for url in urls:
        push(url)
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(3)

    print("방문 종료")
    time.sleep(10)

    while True:
        url = pop()
        if url is None:
            break
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(3)
    print("방문 종료")
