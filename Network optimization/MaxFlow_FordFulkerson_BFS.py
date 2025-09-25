
from collections import deque
class Graph:
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {i: {} for i in range(nodes)}
        
        
    def add_edge(self, s, t, w):
        self.graph[s][t] = w
        
        
    def bfs(self, source, sink, parent):
        visited = [False] * self.nodes
        queue = deque([source])
        visited [source] = True
        
        while queue:
            currentNode = queue.popleft()
            for neighbor, capacity in self.graph[currentNode].items():
                if not visited[neighbor] and capacity >0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = currentNode
                    if neighbor == sink:
                        return True
        return False
    
    
    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = [-1] * self.nodes
        
        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u
                
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                if self.graph[u][v] == 0:
                    del self.graph[u][v]
                if v not in self.graph:
                    self.graph[v] = {}
                self.graph[v][u] = self.graph[v].get(u, 0)+ path_flow
                v = u
            max_flow +=path_flow
                
        return max_flow
    
# ---------------------------
# Example usage
# ---------------------------

g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source, sink = 0, 5
print("The maximum possible flow is:", g.ford_fulkerson(source, sink))
    
            