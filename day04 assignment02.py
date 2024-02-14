## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(nameAry[v], end = ' ')
	print()
	for row in range(g.SIZE) :
		print(nameAry[row], end = ' ')
		for col in range(g.SIZE) :
			print("%2d" % g.graph[row][col], end = ' ')
		print()
	print()


def Max_Vertex(v, visited, value) :
	visited[v] = True
	if value[1] < nameAry[v][1]:
		value = nameAry[v]
	else:
		pass

	for c in range(gSize):
		if G1.graph[v][c] == 1 and not visited[c]:
			value = Max_Vertex(c, visited, value)
	else:
		return value


## 전역 변수 선언 부분 ##
G1 = None
nameAry = [['GS25', 30], ['CU', 60], ['seven11', 10], ['ministop', 90], ['emart24', 40]]
GS25, CU, seven11, ministop, emart24= 0, 1, 2, 3, 4


## 메인 코드 부분 ##
gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU] = 1; G1.graph[GS25][seven11] = 1;
G1.graph[CU][GS25] = 1; G1.graph[CU][ministop] = 1;
G1.graph[seven11][GS25] = 1; G1.graph[seven11][CU] = 1; G1.graph[GS25][ministop] = 1;
G1.graph[ministop][CU] = 1; G1.graph[ministop][seven11] = 1; G1.graph[ministop][emart24] = 1;
G1.graph[emart24][ministop] = 1;

printGraph(G1)
visited = [False]*gSize
value = ['', 0]
print(Max_Vertex(0, visited, value))

