# 🏗️ Data Structures & Algorithms

## Executive Summary
Data Structures & Algorithms (DSA) form the cornerstone of efficient software engineering. This curriculum covers fundamental data structures and algorithms using Python 3.12, with emphasis on algorithmic thinking, complexity analysis, and practical implementation. Students will understand how to choose appropriate data structures and algorithms for real-world problems while mastering analysis techniques for performance optimization.

## Core Concepts
Understanding DSA requires mastery of:
- **Time Complexity**: Big O, Omega, Theta notation for performance analysis
- **Space Complexity**: Memory usage patterns and optimization
- **Data Structure Types**: Linear vs non-linear, mutable vs immutable
- **Algorithm Paradigms**: Divide & conquer, greedy, dynamic programming
- **Searching & Sorting**: Foundational operations on collections
- **Memory Management**: Stack vs heap allocation, garbage collection understanding

### Why This Matters (2024 Perspective)
In 2024-2025, DSA competency directly impacts:
- 60% of FAANG+ interviews focus heavily on DSA (per LeetCode data)
- Python's DSA usage grew 25% in competitive programming (2024 trends)
- Advanced patterns like trie trees powering generative AI applications

## Prerequisites
- Programming Fundamentals (variables, loops, functions, classes)
- Basic Python syntax and built-in data types (lists, dicts, sets)
- Mathematical foundations (algebra, logic)
- Comfort with recursion and iterative problem-solving

## Learning Objectives
- [ ] Analyze algorithm complexity using Big O notation accurately
- [ ] Implement fundamental data structures from scratch
- [ ] Apply optimal algorithms for common problem categories
- [ ] Compare and contrast data structure trade-offs (time vs space)
- [ ] Debug and optimize existing DSA implementations
- [ ] Trace through recursive algorithms manually

## Key Technologies & Tools
| Technology | Version (2024) | Purpose |
|------------|----------------|---------|
| Python    | 3.12          | Native data structures, list comprehensions, generator functions |
| numpy     | 1.26          | Efficient array operations, vectorized computations |
| matplotlib| 3.8           | Algorithm visualization, performance plotting |
| pytest    | 8.0           | DSA testing with parametrization and fixtures |
| timeit    | built-in       | Micro-benchmarking and performance timing |

## Hands-On Example
Let's implement a complete binary search tree with advanced operations:

```python
from typing import Optional, List, Any
from collections import deque

class TreeNode:
    """Binary tree node with parent reference for advanced operations."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None

class BinarySearchTree:
    """Complete BST implementation with advanced operations."""

    def __init__(self):
        self.root: Optional[TreeNode] = None
        self.size = 0

    def insert(self, value: Any) -> None:
        """Insert value into BST maintaining order property."""
        new_node = TreeNode(value)

        if not self.root:
            self.root = new_node
            self.size = 1
            return

        current = self.root
        parent = None

        while current:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                # Duplicate values: store as left child
                current = current.left

        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.size += 1

    def search(self, value: Any) -> Optional[TreeNode]:
        """Search for value in BST. O(log n) average case."""
        current = self.root

        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, value: Any) -> bool:
        """Delete node with given value. Returns True if successful."""
        node = self.search(value)
        if not node:
            return False

        self._delete_node(node)
        self.size -= 1
        return True

    def _delete_node(self, node: TreeNode) -> None:
        """Internal method to delete a specific node."""
        if not node.left and not node.right:
            # Case 1: Leaf node
            self._transplant(node, None)

        elif not node.left:
            # Case 2: Only right child
            self._transplant(node, node.right)

        elif not node.right:
            # Case 3: Only left child
            self._transplant(node, node.left)

        else:
            # Case 4: Two children
            successor = self._min_value_node(node.right)
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _transplant(self, old_node: TreeNode, new_node: Optional[TreeNode]) -> None:
        """Replace one subtree with another."""
        if not old_node.parent:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        if new_node:
            new_node.parent = old_node.parent

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """Find minimum value node in subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal returns sorted list. O(n) time."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List) -> None:
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def level_order_traversal(self) -> List[List[Any]]:
        """BFS traversal by levels. O(n) time, O(w) space."""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    def is_balanced(self) -> bool:
        """Check if tree is height-balanced. O(n) time."""
        return self._check_balance(self.root) >= 0

    def _check_balance(self, node: Optional[TreeNode]) -> int:
        """Return height if balanced, -1 if not."""
        if not node:
            return 0

        left_height = self._check_balance(node.left)
        right_height = self._check_balance(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    def get_height(self) -> int:
        """Calculate tree height. O(log n) for balanced trees."""
        return self._get_height_helper(self.root)

    def _get_height_helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self._get_height_helper(node.left),
                       self._get_height_helper(node.right))

# Demonstrate comprehensive BST usage
def main():
    """Complete demonstration of BST operations."""
    bst = BinarySearchTree()

    # Insert values
    values = [10, 5, 15, 3, 7, 12, 18, 1, 4, 13]
    for val in values:
        bst.insert(val)

    print(f"Tree size: {bst.size}")
    print(f"Tree height: {bst.get_height()}")
    print(f"Is balanced: {bst.is_balanced()}")

    # Search operation
    node = bst.search(7)
    print(f"Found node with value: {node.value if node else 'Not found'}")

    # Traversals
    inorder = bst.inorder_traversal()
    levels = bst.level_order_traversal()
    print(f"Inorder (sorted): {inorder}")
    print(f"Level order: {levels}")

    # Delete operations
    bst.delete(5)  # Node with two children
    bst.delete(18)  # Leaf node
    print(f"After deletions - size: {bst.size}, height: {bst.get_height()}")

if __name__ == "__main__":
    main()
```

This implementation demonstrates:
- **Binary tree traversals**: inorder, level-order with BFS
- **BST operations**: insert, search, delete with all cases
- **Tree balancing**: height calculation and balance checking
- **Parent pointers**: bidirectional navigation
- **Memory efficiency**: O(log n) average time complexity

## Common Pitfalls

### 1. Time Complexity Misunderstanding
```python
# ❌ WRONG: O(n²) complexity analysis
def find_duplicates(nums):  # Assumed O(n) but actually O(n²)
    duplicates = []
    for num in nums:           # O(n)
        if nums.count(num) > 1 and num not in duplicates:  # O(n) inside loop
            duplicates.append(num)
    return duplicates

# ✅ CORRECT: O(n) with hash set
def find_duplicates_optimal(nums):
    seen = set()
    duplicates = set()
    for num in nums:           # O(n)
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)
```

### 2. Recursion Stack Overflow
```python
# ❌ DANGEROUS: Stack overflow with large n
def fibonacci_recursive(n):  # Recursion depth limited (~1000)
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# ✅ EFFICIENT: Iterative approach, O(n) time, O(1) space
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 3. Choosing Wrong Data Structure
```python
# ❌ INEFFICIENT: List for set operations
frequent_items = list(set(items))  # O(n) space, slow membership checks

# ✅ EFFICIENT: Set for constant-time lookups
frequent_items = set(items)  # O(n) space, O(1) average lookup
```

## Best Practices (2024 Standards)

### Algorithm Selection
- **Space vs Time Trade-offs**: Choose based on constraints (mobile vs cloud)
- **Worst-case vs Average-case**: Consider your data distribution
- **Constant Factors**: Big O hides implementation details
- **Cache Friendliness**: Prefer sequential over random memory access

### Implementation Quality
- **Defensive Programming**: Validate inputs, handle edge cases
- **Type Safety**: Use strong typing for complex data structures
- **Documentation**: Comment algorithmic choices and complexity
- **Testing**: Comprehensive test cases including edge cases

### Performance Analysis
- **Benchmark**: Measure against different inputs and environments
- **Profile**: Use `cProfile` for Python performance analysis
- **Optimize**: Focus on bottlenecks identified by profiling
- **Monitor**: Track performance in production environments

## Advanced Topics

### Self-Balancing Trees (AVL/Red-Black)
```python
# AVL Tree rotation example
def rotate_left(node):
    """Single left rotation for AVL balancing."""
    new_root = node.right
    node.right = new_root.left
    if new_root.left:
        new_root.left.parent = node
    new_root.left = node
    new_root.parent = node.parent
    node.parent = new_root

    # Update heights (implementation details)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root
```

### Graph Algorithms Implementation
```python
from collections import defaultdict, deque

class Graph:
    """Graph with comprehensive algorithm implementations."""
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def bfs(self, start):
        """Breadth-First Search. O(V + E) time."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs_iterative(self, start):
        """Depth-First Search (iterative). O(V + E) time."""
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Reverse to maintain order
                stack.extend(reversed(self.adj_list[vertex]))

        return result

    def topological_sort(self):
        """Kahn's algorithm for DAG topological sort."""
        incoming = {node: 0 for node in self.adj_list}
        for neighbors in self.adj_list.values():
            for neighbor in neighbors:
                incoming[neighbor] += 1

        queue = deque([node for node in incoming if incoming[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj_list[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == len(incoming) else None  # None if cycle
```

### Advanced Sorting Algorithms
```python
def quicksort(arr, low=0, high=None):
    """Quicksort with median-of-three pivot. O(n log n) average."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    """Partition with median-of-three pivot selection."""
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort()  # Median value
    pivot_value, pivot_idx = pivot_candidates[1]

    # Move pivot to end
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

## Complexity Analysis & Big-O Notation

### Time Complexity Analysis
- Best, average, and worst case analysis
- Space complexity: auxiliary vs total space, in-place algorithms
- Amortized analysis: aggregate, accounting, potential methods
- Master theorem for divide-and-conquer recurrences
- Big-O, Big-Θ, Big-Ω notations and growth rates comparison
- Practical performance vs theoretical complexity

## Fundamental Data Structures

### Arrays and Lists
- Static vs dynamic arrays and resizing strategies
- Memory layout and contiguous storage
- Linked lists: singly, doubly, circular implementations
- Skip lists for probabilistic balancing

### Stack and Queue Operations
- Stacks: LIFO operations, call stack mechanics
- Expression evaluation using stacks
- Queues: FIFO, circular queues, priority queues
- Deques for double-ended operations

### Hash Tables and Trees
- Hash tables: collision resolution strategies
- Load factor management and rehashing
- Binary trees, BST properties, balanced trees
- Heaps and priority queues, tries and prefix trees

## Graph Algorithms & Network Analysis

### Graph Representations
- Adjacency matrix vs adjacency list trade-offs
- Sparse vs dense graph considerations
- Edge list representations

### Traversal Algorithms
- DFS: recursive and iterative implementations
- Topological sort for DAGs
- Connected components identification
- BFS: shortest path in unweighted graphs
- Level-order traversal patterns

### Path Finding Algorithms
- Dijkstra's algorithm: single-source shortest path
- A\* search: heuristic search with admissible heuristics
- Bellman-Ford for negative edges
- Network flow: Ford-Fulkerson method
- Maximum matching in bipartite graphs

## Dynamic Programming & Optimization

### DP Principles
- Optimal substructure property
- Overlapping subproblems identification
- Memoization vs tabulation approaches
- Top-down vs bottom-up implementations

### Classic DP Problems
- 0/1 Knapsack problem
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Edit distance (Levenshtein)
- Matrix chain multiplication

### Advanced DP Techniques
- State space optimization with rolling arrays
- Space-efficient DP implementations
- Digit DP for numerical problems
- Bitmask DP for subset problems
- Probability DP for stochastic processes

## Probabilistic & Approximate Structures

### Bloom Filters
- False positive probability analysis
- Optimal hash function selection
- Multiple hash functions implementation
- Space-efficient membership testing

### Sketching Algorithms
- Count-Min sketch for frequency estimation
- Heavy hitters identification
- HyperLogLog for cardinality estimation
- Distributed counting with merging

### Probabilistic Data Structures
- Skip lists: probabilistic balanced search trees
- Consistent hashing for distributed systems
- Load balancing in distributed environments

## Caching Strategies & Implementation

### Cache Replacement Policies
- LRU (Least Recently Used) implementation
- LFU (Least Frequently Used) tracking
- FIFO (First In First Out) queues
- Random replacement strategies

### LRU Implementation Techniques
- Doubly linked list with hash map
- Time complexity analysis (O(1) operations)
- Memory overhead considerations

### Cache-Aware Optimization
- Blocking algorithms for cache efficiency
- Tiling for matrix operations
- Memory access pattern optimization
- Spatial vs temporal locality principles

### Memory Hierarchy
- CPU cache levels (L1, L2, L3)
- Main memory vs disk storage
- Cache-friendly data structure design
- Memory bandwidth optimization

## Related Concepts

### Prerequisites
- [Programming Fundamentals](../00-basics/programming-fundamentals.md)
- [Mathematical Foundations](../00-math/math-for-programmers.md)

### Next Level Topics
- [Advanced Data Structures](../02-advanced/graphs-trees-advanced.md)
- [Algorithm Design Paradigms](../03-advanced/dynamic-programming.md)
- [Competitive Programming](../04-spec/competitive-coding.md)

### Complementary Skills
- [Performance Analysis](../backend-systems/performance-engineering.md)
- [System Design](../architecture/system-design-interviews.md)

## Resources

### Books
- **Introduction to Algorithms (CLRS, 4th Edition, 2024)** by Cormen et al.
  \$89.99, 1,344 pages, MIT Press - Comprehensive algorithmic foundation
- **Algorithms (Sedgewick, 2024)** by Robert Sedgewick and Kevin Wayne
  \$79.99, 968 pages, Addison-Wesley - Clean implementations in Java
- **Grokking Algorithms (2nd Edition)** by Aditya Bhargava
  \$49.99, 256 pages, Manning - Visual approach for beginners

### Courses
- **Data Structures & Algorithms Specialization** - University of California San Diego (Coursera)
  Coursera, 6 months, \$49/month - Comprehensive DSA with Python implementations
- **Advanced Algorithms and Complexity** - University of California San Diego (Coursera)
  Coursera, 6 weeks, \$49 - Theoretical foundations of algorithms
- **Algorithmic Toolbox** - University of California San Diego (Coursera)
  Coursera, 6 weeks, \$49 - Problem-solving techniques and patterns

### Documentation
- **Python Data Structures Official Guide** - docs.python.org
  Free, detailed documentation - Built-in types and their complexity
- **Big-O Complexity Cheat Sheet** - bigocheatsheet.com
  Free visualization - Quick reference for common operations
- **VisuAlgo** - visualgo.net
  Free interactive website - Algorithm animations and examples

### Practice Platforms
- **LeetCode** - leetcode.com (premium recommended)
- **CodeForces** - codeforces.com
- **HackerRank** - hackerrank.com
- **GeeksForGeeks Practice** - practice.geeksforgeeks.org

## Assessment Criteria

### Theoretical Understanding
- ✅ Can derive time/space complexity for basic algorithms
- ✅ Explains Big O, Omega, Theta notation differences accurately
- ✅ Identifies algorithm trade-offs (time vs space vs simplicity)
- ✅ Describes how hashing distributes elements uniformly
- ✅ Analyzes recursion call stack depth and memory implications

### Implementation Skills
- ✅ Implements fundamental data structures from scratch
- ✅ Handles edge cases properly (empty inputs, duplicates, large datasets)
- ✅ Applies appropriate algorithms for sorting/searching problems
- ✅ Optimizes code for memory efficiency and cache locality
- ✅ Uses proper error handling for malicious inputs

### Problem-Solving Ability
- ✅ Recognizes problem patterns (two-pointer, sliding window, etc.)
- ✅ Converts complex problems into graph/tree representations
- ✅ Applies greedy algorithms correctly with justification
- ✅ Decomposes dynamic programming problems into subproblems
- ✅ Identifies when brute force becomes unacceptable

### Optimization Techniques
- ✅ Improves algorithm time/space complexity incrementally
- ✅ Identifies bottlenecks using profiling tools
- ✅ Applies algorithmic optimizations (memoization, pruning)
- ✅ Balances readability with performance requirements
- ✅ Considers hardware constraints (cache, memory bandwidth)

### Practical Application
- ✅ Selects optimal data structures for specific use cases
- ✅ Implements thread-safe data structures when needed
- ✅ Measures and benchmarks algorithm performance
- ✅ Documents complexity assumptions and limitations
- ✅ Maintains production-ready code with proper testing

### Career Readiness Indicators
- **Junior Developer**: Solves LeetCode medium problems independently
- **Mid-Level Engineer**: Optimizes algorithms for production constraints
- **Senior Engineer**: Designs scalable system architectures
- **Interview Ready**: Explains solutions with multiple approaches and trade-offs
