## 함수 선언 부분 ##
class Treenode:
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

root = None
name_ary = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스', '잇지', '여자친구']

node = Treenode()
node.data = name_ary[0]
root = node

for name in name_ary[1:]:

    node = Treenode()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else :
            if current.right is None:
                current.right = node
                break
            current = current.right

find_name = input("찾을 아이돌 그룹이름 입력: ")

current = root
while True:
    if find_name == current.data:
        print(find_name, '을(를) 찾음.')
        break
    elif find_name < current.data :
        if current.left is None :
            print(find_name, '이(가) 트리에 없음')
            break
        current = current.left
    else :
        if current.right is None :
            print(find_name, '이(가) 트리에 없음')
            break
        current = current.right
