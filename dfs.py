#dfs
graph = {
'A':['B','C','D'],
'B':['E','F'],
'C':['G','H'],
'D':['I'],
'E':[],
'F':['J'],
'G':[],
'H':[],
'I':['K','L'],
'J':[],
'K':[],
'L':[]
}
visited = set()
def dfs(visited, graph, node):
 if node not in visited:
  print (node)
  visited.add(node)
 for neighbour in graph[node]:
    dfs(visited, graph, neighbour)
print("Depth-First Search")
dfs(visited, graph, 'A')
