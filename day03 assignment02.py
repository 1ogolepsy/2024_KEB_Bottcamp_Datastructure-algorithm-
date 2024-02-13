# 자료구조 알고리즘, 이진트리 제외 각 쳅터의 연습문제 풀기
import random
import math

class Node() :
	def __init__ (self) :
		self.data = None
		self.rlink = None
		self.llink = None

def printNodes(start, mode):
	current = start

	if mode == 1:
		if current.rlink == None:
			return
		print(current.data, end=' ')
		while current.rlink != None:
			current = current.rlink
			print(current.data, end=' ')
	elif mode == 0:
		if current.llink == None:
			return
		print(current.data, end=' ')
		while current.llink != None:
			current = current.llink
			print(current.data, end=' ')
	print()


data_array = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":
	head, current, pre = None, None, None

	node = Node()
	node.data = data_array[0]
	head = node

	current = head
	for value in data_array[1:]:
		node = Node()
		node.data = value
		node.llink = current
		current.rlink = node
		current = node

	printNodes(head, 1)
	printNodes(current, 0)