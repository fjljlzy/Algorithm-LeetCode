# Mock Interview Questions

### 4. Graph

#### 4.1 basis:

- Vertices and Edges
- Direct and undirected graph
- Weighted and unweighted graph
- DAG: Directed acyclic graph / Topological Sort
- Traverse: BFS(deque), DFS(recursion call)
- Minimum Spanning Tree

#### 4.2 Some related problems:

##### Q1.  DFS and BFS are two basic methods to traverse a data structure like tree or a graph. What's the additional part of these two algorithms in graph compared to tree？Why DFS and BFS in tree don't have this?

Ans: We need to add a set which stored the node we have already visited. Otherwise the traverse path may have a loop. In tree we don't do this because tree has no cycle.

##### Q2. BFS can find shortest paths from the starting node to any other nodes. Briefly talk about how it works.

Ans: We can imagine we throw a stone into the river, it will produce a water wave spread from center to outside. BFS is like water wave, which spread from starting node to any other node with the same speed. For each iteration, once the node is visited, the shortest path is fixed. If it can't be visit, it means one iteration is not enough, we need more distance to visit the node. BFS algorithm here is like to traverse the graph one layer and one layer from inside to outside.

##### Q3. For some problems, suppose DFS and BFS both can work, can you tell the performance differences of DFS and BFS?

Ans: If some solutions are close to root, choose BFS. If solutions are deep but frequent, choose DFS.

##### Q4. What is Topological Sort, what's the relationship of Topological Sort with DAG?

Ans: A directed acyclic graph (DAG) can represent order of doing things, Topological Sort can sort the node into a list which every node will obey the order shown in DAG. If (u,v) is an edge, then u must happen before v.

##### Q5. How Topological Sort works, how to use DFS to perform Topological Sort?

Ans: DFS will call DFS recursively until it find the deepest node, when it exits, we append the current node into a stack. Finally we reverse the stack, which is the correct order of topological sort. (See wikipedia)

##### Q6. 

