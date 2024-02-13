def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear != SIZE-1) :
		return False
	elif (rear == SIZE -1) and (front == -1) :
		return True
	else :
		for i in range(front+1, SIZE) :
			queue[i-1] = queue[i]
			queue[i] = None
		front -= 1
		rear -= 1
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		return
	rear += 1
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		return None
	front += 1
	data = queue[front]
	queue[front] = None

	for i in range(front + 1, SIZE):
		queue[i - 1] = queue[i]
		queue[i] = None
	front -= 1
	rear -= 1

	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

## 전역 변수 선언 부분 ##
SIZE = 5
queue = ['정국', '뷔', '지민', '진', '슈가']
front = -1
rear = 4

## 메인 코드 부분 ##
if __name__ == "__main__" :
	print(f'대기줄 상태 : {queue}')
	while True:
		print(f'{deQueue()}님 식당에 들어감.')
		print(f'대기줄 상태 : {queue}')
		if isQueueEmpty():
			print('식당 영업 종료!')
			break