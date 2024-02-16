## 함수 선언 부분 ##
import random
count = 0
def bubbleSort(ary) :
	global count
	n = len(ary)
	for end in range(n-1, 0, -1) :
		changeYN = False
		count += 1
		print('#사이클-->', ary)
		for cur in range(0, end) :
			if (ary[cur] > ary[cur+1]) :
				ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
				changeYN = True
		if not changeYN :
			break
	return ary

## 전역 변수 선언 부분 ##
dataAry = [random.randint(0,200) for _ in range(20)]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = bubbleSort(dataAry)
print('정렬 후 -->', dataAry)
print(count)
