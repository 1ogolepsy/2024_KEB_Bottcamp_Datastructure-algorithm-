## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def print_node(start):
	current = start
	value = ''
	value += current.data + ' '
	if current.left is not None:
		value += print_node(current.left)
	if current.right is not None:
		value += print_node(current.right)

	return value
def find(find_name):
	global root
	current = root
	parent = None

	while True:
		if find_name == current.data:
			return True
		elif find_name < current.data:
			if current.left == None:
				return False
			parent = current
			current = current.left
		else:
			if current.right == None:
				return False
			parent = current
			current = current.right

root = None
name_ary = ['레쓰비 캔커피', '레쓰비 캔커피', '레쓰비 캔커피', '도시락', '도시락', '삼각김밥', '레쓰비 캔커피', '도시락', '코카콜라', '삼다수', '레쓰비 캔커피', '레쓰비 캔커피', '레쓰비 캔커피', '츄파춥스', '츄파춥스', '레쓰비 캔커피', '코카콜라', '큐파춥스', '삼각김밥', '코카콜라']

node = TreeNode()
node.data = name_ary[0]
root = node

for name in name_ary[1:]:
	if find(name):
		continue
	node = TreeNode()
	node.data = name
	current = root
	while True:
		if name < current.data:
			if current.left == None:
				current.left = node
				break
			current = current.left
		else:
			if current.right == None:
				current.right = node
				break
			current = current.right
print(f'오늘 판매된 종류(중복X) -- > {print_node(root)}')