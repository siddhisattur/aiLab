#bfs
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
visited = []
queue=[]
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
 g = queue.pop(0)
 print (g, end = " ")
 for neighbour in graph[g]:
   if neighbour not in visited:
     visited.append(neighbour)
 queue.append(neighbour)
print("Breadth-First Search")
bfs(visited, graph, 'A')
