from queue import PriorityQueue

v = 10
graph = [[] for _ in range(v)]

def bestfs(act_source, target, v):
    vis = [False] * v
    pq = PriorityQueue()
    pq.put((0, act_source))
    vis[act_source] = True
    print("Optimal Path:")
    
    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ")
        
        if u == target:
            break
        
        for v, c in graph[u]:
            if not vis[v]:
                vis[v] = True
                pq.put((c, v))
    
    print()

def addedge(u, v, h):
    graph[u].append((v, h))
    graph[v].append((u, h))

addedge(0, 1, 12)
addedge(0, 2, 4)
addedge(1, 3, 7)
addedge(1, 4, 3)
addedge(2, 5, 8)
addedge(2, 6, 2)
addedge(5, 7, 4)
addedge(6, 8, 9)
addedge(6, 9, 0)

source = 0
target = 9

bestfs(source, target, v)
