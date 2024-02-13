## 함수 선언 부분 ##
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		return False
	top += 1
	stack[top] = data
	return True

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("스택이 비었습니다.")
		return None
	return stack[top]

## 전역 변수 선언 부분 ##
SIZE = int(input("과자집에 도착할 때까지 떨어뜨릴 돌의 개수를 입력하세요 ==> "))
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
	rock = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
	print("과자집에 가는길 : ", end = ' ')
	for i in rock:
		if push(i):
			print(f'{i} -->', end = ' ')
	print('과자집')

	input("우리집으로 돌아가기 시작하려면 아무거나 입력하세요.")

	print("우리집에 가는길 : ", end = ' ')
	while True:
		temp = pop()
		if temp is None:
			break
		print(f'{temp} -->', end = ' ')
	print('우리집')