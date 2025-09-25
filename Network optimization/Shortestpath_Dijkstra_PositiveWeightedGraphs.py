# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 19:42:01 2025

@author: hadis
"""

import heapq

def dijkstra(graph, start):
    # Distance dictionary
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    # Predecessor dictionary (for path reconstruction)
    prev = {node: None for node in graph}
    
    # Min-heap priority queue
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = node   # store how we reached this neighbor
                heapq.heappush(heap, (new_cost, neighbor))

    return dist, prev


def get_path(prev, target):
    """Reconstruct path from start to target using predecessor dictionary."""
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]   # reverse order


# Example graphs
graph1 = {
    'A': [('B', 1), ('C', 3)],
    'B': [('C', 3), ('D', 5)],
    'C': [('D', 10)],
    'D': []
}

graph2 = {
    'A': [('B', 1), ('C', 3)],
    'B': [('C', 3), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Run Dijkstra on graph1
dist1, prev1 = dijkstra(graph1, 'A')
print("Graph1 distances:", dist1)
print("Shortest path A→D:", get_path(prev1, 'D'))

# Run Dijkstra on graph2
dist2, prev2 = dijkstra(graph2, 'A')
print("Graph2 distances:", dist2)
print("Shortest path A→D:", get_path(prev2, 'D'))
