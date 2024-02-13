
class Node:
    def __init__ (self):
        self.data = None
        self.link = None

def print_nodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def insert_node(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node

def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data:         # 첫 번째 노드 삭제
        current = head
        head = head.link
        del(current)
        print("첫 번째 노드가 삭제됨")
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del(current)
            print("중간 노드가 삭제됨")
            return

    print(f"{delete_data}은/는 삭제할 수 없음")

def find_node(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current
    return Node()

def make_simple_linked_list(name_phone):
    global memory, head, current, pre
    print_nodes(head)

    node = Node()
    node.data = name_phone
    memory.append(node)
    if head is None:
        head = node
        return

    if head.data[1] > name_phone[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data[1] > name_phone[1]:
            pre.link = node
            node.link = current
            return

    current.link = node

memory = []
head, current, pre = None, None, None
data_array = [["지민", "180"], ["정국", "177"], ["뷔", "183"], ["슈가", "175"], ["진", "179"]]

if __name__ == "__main__":
    for data in data_array:
        make_simple_linked_list(data)

    print_nodes(head)