# Mock Interview Questions

### 1. Data Structures

#### 1.1 basis：

- (List)Array —> Stack, Queue
- Linked List —> Binary Tree —> Heap —> Graph
- hash table—Dictionary, Set 

#### 1.2 some application problems:

##### Q1. For these different data structures, we have some basic operations, like Construct, Access, Insert, Delete, Search, what are the time complexity of these operations of the corresponding data structures?

Ans: 

##### Q2. We know that in Python we can just use a list to achieve the function of Array or Stack. If we want to use Queue, we can use collections.deque, which is a built-in method in Python. However, can you implement the queue with two stacks? It should have two function: append the value to the tail and pop the head value of the queue. You can just briefly talk about your idea. 

Ans: We have two stacks, in python is two lists. the first stack supports insert operations, and the second stack supports delete operations. For the function append tail, we just append a value to stack 1, for the function pop head, we do a iteration, each time append the value pop from the stack 1 into the stack2, this method make the tail of stack 2 is the head of stack 1. So pop head of the queue, is just pop the tail of stack2.   

##### Q3. Give you a array with many numbers. How to construct it into a linked list?

Ans: First define a Node Class, which includes attributes of value of node and next pointer of the node. Then use iteration, each number of array we construct a node. Finally we return the head node of our linked list.

##### Q4. How to judge a linked list have a ring?

Ans: Use two pointers with fast speed and slow speed. If the linked list with no ring, fast pointer will arrive the end of the linked list before slow pointer, they will never meet. However if there is a ring, fast pointer will catch the slow pointer later in the same node.

##### Q5. Give you a tree, how to find the biggest value of this tree?

Ans: We need to traverse through this tree. There are two methods, DFS(pre-order, in-order, post-order) and BFS. We have recursion and iteration two implement methods to get the answer.

##### Q6. How recursion works in our system?

Ans: Stack realized by system. Suppose we are calling a recursive function,  we can name it father function. Then memory stack push  this process of father function. This recursive function calls itself, we can name it son function, then memory stack push the process of son function. Our system handles the tail of memory stack. Once the process of son function is done, it return the result to its caller: father function then pop from the memory stack. Father function receives the return of its son function, and it return the result to us and pop from the memory stack. Now memory stack is null and recursion is done.

##### Q7. What's the relationship between recursion and iteration?

Ans: All recursion can be done in iteration. But recursion versions can be more intuitive once you are familiar with it.

##### Q8. How to reversed print a linked list?

Ans: Two methods. Iterative approach: traverse the linked list and save each value in an array, reverse the array. Recursion: just call the next node until null, then print the value. Why it works? Memory Stack.

##### Q9. How to rewrite recursion into iteration?

Ans: Hard problem. We know that idea is simple, recursion can be done in iteration with memory stack. But sometimes the problems can be solved by recursion easily and more intuitively, while change it into iteration version is more tricky. My personal idea is that for specific issues we have specific rewriting methods. 

