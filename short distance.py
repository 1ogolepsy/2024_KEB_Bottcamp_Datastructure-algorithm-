class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def find_short_distance_in_n_city(g, distance, start):
    global count_distance, answer_arr
    count_distance += 1

    if count_distance > distance:
        count_distance -= 1
        return
    elif count_distance < distance:
        answer_arr[start] = -1

    if count_distance == distance and answer_arr[start] != -1:
        answer_arr[start] = distance

    for i in range(len(g.graph)):
        if g.graph[start][i] == 1 :
            find_short_distance_in_n_city(g, distance, i)

    count_distance -= 1

def array_to_index(arr, d):
    result = []
    for i in range(len(arr)):
        if arr[i] == d:
            result.append(i + 1)

    if not result:
        return -1
    return result

string = input("N, M, K, X를 입력하세요: ")
base_arr = string.split(' ')

N = int(base_arr[0])
M = int(base_arr[1])
K = int(base_arr[2])
X = int(base_arr[3]) - 1

g1 = Graph(N)

count_distance = -1;
answer_arr = [None for _ in range(N)]

for i in range(M):
    arr = input("연결할 노드를 입력하세요. start end: ").split(' ')

    g1.graph[int(arr[0]) - 1][int(arr[1]) - 1] = 1

find_short_distance_in_n_city(g1, K, X)
print(array_to_index(answer_arr, K))
