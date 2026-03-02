<h2 align="center">Depth First Search</h1>

## Overview

**Depth First Search (DFS)** is a graph traversal algorithm used to explore nodes and edges of a graph or tree. It starts from a source node and explores as far as possible along each branch before backtracking.

DFS is commonly used in:

* Path finding
* Cycle detection
* Topological sorting
* Connected component detection
* Maze solving

<a href="/src/main.py">Check out for source code</a>

---

## 🧠 How DFS Works

DFS follows this strategy:

1. Start at a chosen node (root/source).
2. Visit the node and mark it as visited.
3. Move to one of its unvisited neighbors.
4. Repeat until no unvisited neighbors remain.
5. Backtrack to explore remaining branches.

DFS can be implemented using:

* **Recursion** (uses call stack)
* **Explicit stack data structure**

---

## ⏱ Time and Space Complexity

| Case  | Complexity   |
| ----- | ------------ |
| Time  | **O(V + E)** |
| Space | **O(V)**     |

Where:

* **V** = number of vertices
* **E** = number of edges

---

## 🧩 DFS Example

### Graph Representation

```
A → B → D
↓
C → E
```

### DFS Traversal (starting from A)

```
A → B → D → C → E
```

---

## 💻 Example Implementation (Python)

### Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
```

### Iterative DFS (Using Stack)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors in reverse order for same traversal as recursion
            stack.extend(reversed(graph[node]))
```

---

## 🧪 Sample Graph Input

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

dfs_recursive(graph, 'A')
# Output: A B D C E
```

---

## 🌍 Real-World Applications

* Social network connection exploration
* File system traversal
* Web crawling
* Solving puzzles (e.g., Sudoku, mazes)
* Finding strongly connected components

---

## ✅ When to Use DFS

Use DFS when:

* You need to explore all possible paths
* Memory is limited (compared to BFS in wide graphs)
* You want to detect cycles or components
* You need topological ordering

---

## 📚 Summary

DFS is a fundamental graph traversal technique that explores deeply before moving sideways. It is efficient, simple to implement, and forms the backbone of many advanced graph algorithms.

