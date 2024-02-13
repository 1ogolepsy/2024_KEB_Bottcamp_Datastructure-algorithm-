## 함수 선언 부분 ##
def is_queue_full():
    global size, queue, front, rear
    if (rear+1) % size == front:
        return True
    else:
        return False
def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else :
        return False

def en_queue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % size
    queue[rear] = data

def de_queue():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front+1) % size]

size = int(input("큐의 크기를 입력하세요 ==> "))
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__":
    menu = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (menu != 'X' and menu != 'x'):
        if menu== 'I' or menu == 'i':
            data = input("입력할 데이터 ==> ")
            en_queue(data)
            print("큐 상태 : ", queue)
        elif menu== 'E' or menu == 'e':
            data = de_queue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        elif menu== 'V' or menu == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        else :
            print("입력이 잘못됨")

        menu = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
