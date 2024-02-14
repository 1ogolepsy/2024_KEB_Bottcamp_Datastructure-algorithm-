graph = [
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 0],
	[0, 1, 0, 0, 0],
	[1, 1, 0, 0, 1],
	[0, 0, 1, 1, 0]
]


def dfs(g, v, visited):
	visited[v] = True
	print(v, end= ' ')
	for i in range(len(graph)):
		if graph[v][i] == 1 and not visited[i]:
			dfs(g, i, visited)
	return

visited = [0] * len(graph)
dfs(graph, 0, visited)