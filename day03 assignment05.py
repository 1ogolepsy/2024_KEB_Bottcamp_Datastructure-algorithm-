def isQueueFull():
	global SIZE, queue, front, rear
	if ((rear + 1) % SIZE == front):
		return True
	else:
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear):
		return True
	else:
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		return None
	rear = (rear + 1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None

	for i in range(front + 1, SIZE):
		queue[i - 1] = queue[i]
		queue[i] = None
	front -= 1
	rear -= 1

	return data

def print_waiting_time():
	global SIZE, queue, front, rear
	waiting = 0

	for data in queue[front:rear]:
		if data is not None:
			waiting += data[1]

	print(f'귀하의 대기 예상시간은 {waiting}분입니다.')
	print(f'현재 대기 콜 --> {queue}')

def plus_waiting():
	global SIZE, queue, front, rear

	if isQueueFull():
		print('현재 대기줄이 모두 찼습니다. 나중에 다시 걸어주세요.')

	job = input('''전화로 수행할 작업의 번호를 입력하세요
	1) 사용문의
	2) 고장문의
	3) 환불문의
	4) 기타문의
	: ''')

	enQueue(job_waiting[int(job) - 1])
## 전역 변수 선언 부분 ##
SIZE = 6
queue = [None for _ in range(SIZE)]
job_waiting = [('사용', 9), ('고장', 3), ('환불', 4), ('기타', 1)]
front = 0
rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
	while True:
		plus_waiting()
		print_waiting_time()