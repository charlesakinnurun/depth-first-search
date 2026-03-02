"""
Depth First Search (DFS) Implementation and Visualization
---------------------------------------------------------
This project demonstrates how DFS works on graphs using both 
Recursive and Iterative approaches. It includes visual 
illustrations of the traversal process.
"""

import time

class Graph:
    def __init__(self):
        # We use an adjacency list to represent the graph.
        # Format: { 'A': ['B', 'C'], 'B': ['D'], ... }
        self.graph = {}

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # Ensure v exists in the graph keys even if it has no neighbors
        if v not in self.graph:
            self.graph[v] = []

    def display_graph_structure(self):
        """Prints an ASCII illustration of the graph connections."""
        print("\n--- GRAPH STRUCTURE ---")
        for node in self.graph:
            neighbors = ", ".join(self.graph[node]) if self.graph[node] else "End"
            print(f"  [{node}] ---> {neighbors}")
        print("-----------------------\n")

    def dfs_recursive(self, start_node, visited=None):
        """
        Logic: Uses the system call stack to dive deep into branches.
        Complexity: O(V + E) where V is vertices and E is edges.
        """
        if visited is None:
            visited = set()

        # 1. Mark the current node as visited
        visited.add(start_node)
        print(f" Visiting: {start_node} (Recursive)")

        # 2. Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                # 3. If neighbor not visited, dive into that branch immediately
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start_node):
        """
        Logic: Uses an explicit Stack (LIFO) to manage traversal.
        """
        visited = set()
        # The stack stores nodes to be explored
        stack = [start_node]

        print("\nStarting Iterative DFS Stack Trace:")
        while stack:
            # 1. Pop the last element added (LIFO behavior)
            current = stack.pop()

            if current not in visited:
                # 2. Mark as visited
                print(f" Pop & Visit: {current} | Stack: {stack}")
                visited.add(current)

                # 3. Push neighbors to stack (reversed to maintain order similar to recursion)
                for neighbor in reversed(self.graph.get(current, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        print("DFS Iterative Complete.\n")

def run_example():
    """
    Example Graph Illustration:
          A
         / \
        B   C
       / \   \
      D   E   F
    """
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    g.display_graph_structure()

    print("--- RUNNING RECURSIVE DFS (Start from A) ---")
    # Expected: A -> B -> D -> E -> C -> F
    g.dfs_recursive('A')

    print("\n--- RUNNING ITERATIVE DFS (Start from A) ---")
    g.dfs_iterative('A')

    # Visual Animation/Step-by-Step Logic
    print("--- VISUALIZING THE 'DEPTH' CONCEPT ---")
    path = ['A', 'B', 'D']
    print("Path taken to find the bottom of the first branch:")
    for i, node in enumerate(path):
        indent = "  " * i
        print(f"{indent}└─> {node} (Level {i})")
        time.sleep(0.3)
    print("Backtracking now to find next unvisited neighbor...")

if __name__ == "__main__":
    run_example()