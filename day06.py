from collections import deque
graph = [
	[0, 1, 1, 0, 0, 0, 0, 0],
	[1, 0, 0, 1, 0, 0, 0, 0],
	[1, 0, 0, 1, 0, 0, 0, 0],
	[0, 1, 1, 0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0, 1, 0, 0],
	[0, 0, 0, 1, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 1, 0]
]

def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = True
    while queue:
        i = queue.popleft() #O(1)
        print(chr(ord('A')+i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = 1


def dfs(g, v, visited):
	visited[v] = True
	print(v, end= ' ')
	for i in range(len(graph)):
		if graph[v][i] == 1 and not visited[i]:
			dfs(g, i, visited)
	return

visited = [0] * len(graph)
bfs(graph, 0, visited)