# Mock Interview Questions

### 5. Dynamic Programming

#### 5.1 basis:

- Defenition
- LCS (Longest common subsequence problem)
- Knapsack problem

#### 5.2 problems:

##### Q1. What's the essence of dynamic programming?

Ans: Solving complex problems by decomposing the original problem into relatively simple subproblems.

##### Q2. When we solve the Fibonacci problem, we have two methods, recursion and iteration, which one do you think is better, why?

Ans: Iteration. Because during recursion, the same position will be computed redundantly. So if we just simply use recursion, its time complexity is higher than iteration,

##### Q3. Thus, for the Fibonacci problem, can you find a way to improve the performance of recursion approach?

Ans: Yes, we can use memory to store the state or position we have processed before, we can use a dictionary or built-in cache to improve the algorithm in Python.

##### Q4. What's the key points to write the dynamic programing in iterative version?

Ans: 

1. Construct “dependency” graph 
1. Compute the value of each position iteratively according to the topological order of position.