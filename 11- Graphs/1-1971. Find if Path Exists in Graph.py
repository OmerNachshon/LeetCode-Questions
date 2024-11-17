"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

"""
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edge_map = defaultdict(set) # make graph of the edges
        visited = set()
        for s,d in edges:
            edge_map[s].add(d)
            edge_map[d].add(s)

        def visit(num):
            visited.add(num)
            if num == destination:
                return True
            for edge in edge_map[num]:
                if edge not in visited:
                    if visit(edge):
                        return True
            return False
        return visit(source)



# Iterative DFS with Stack
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)

        return False



# BFS With Queue
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)

        return False # Time: O(N + E), Space: O(N + E)
