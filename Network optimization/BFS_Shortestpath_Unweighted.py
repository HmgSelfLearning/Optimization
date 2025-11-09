# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 22:06:41 2025

@author: hadis
"""

from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Queue to store (current_node, path_to_node)
    queue = deque([(start, [start])]) # it should tuples() inside an iterable [] because each path is correspondes to each node pas one tuple
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        
        if current_node == goal:
            return path
        
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found


# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example usage
start_node = 'A'
goal_node = 'F'
path = bfs_shortest_path(graph, start_node, goal_node)
print("Shortest path from", start_node, "to", goal_node, "is:", path)
