# CMPS 2200 Recitation 10## Answers

**Name:** Hrishi Kabra  
**Name:** Petra Radmanovic


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?

    - $O(n + m)$ - each node is visited at most once - for each node that has been visited you then look at all of its neighbours - in an undirected graph each edge would be examined at most twice - once from each endpoint - hence $O(n)$ for nodes + $O(m)$ for edges = $O(n+m)$

- **4)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

    - In a connected graph - any starting node should be able to reach all other nodes - 1 call to reachable from any node - check if the result set size is equal to total number of nodes - if they match then the graph is connected - if not then it is disconnected - hence only 1 call is needed for any case

- **5)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

    - connected makes one call to reachable - this has work of $O(n+m)$ - additional operations in connected such as selecting a starting node, comparing set sizes, etc. are all $O(1)$ - hence work of connected is $O(n+m)$

- **7)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

    - Adjacency matrix stores the graph in an $n \times n$ matrix - to find neighbours of a node you need to go through entire row/col of a matrix - this would take $O(n)$ time - because you are also visiting n nodes and for each nodes you are finding the neighbours this would be $O(n)$ per node or $O(n \times n)$ total - hence work would be equal to $O(n^2)$ - this is worse than what we had earlier