# 자료구조 알고리즘, 이진트리 제외 각 쳅터의 연습문제 풀기
import random
import math

class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def insert_node(data):
	global head, current, pre, last

	def distance(node):
		return math.sqrt(pow(node.data[1],2) + pow(node.data[2],2))

	node = Node()
	node.data = data
	if distance(head) > distance(node):
		node.link = head
		current = head
		while current.link is not head:
			pre = current
			current = current.link
		current.link = node
		head = node
		return

	current = head
	while current.link is not head:
		pre = current
		current = current.link
		if distance(current) > distance(node):
			node.link = current
			pre.link = node
			return

	current.link = node
	node.link = head


if __name__ == "__main__":
	data_array = [(chr(65+i), random.randint(1, 100), random.randint(1, 100)) for i in range(10)]
	head, current, pre, last = None, None, None, None

	node = Node()
	node.data = data_array[0]
	node.link = node
	head = node

	for value in data_array[1:]:
		insert_node(value)

	printNodes(head)
