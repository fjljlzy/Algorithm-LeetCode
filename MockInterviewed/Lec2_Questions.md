# Mock Interview Questions

### 2. Sorting Algorithms

#### 2.1 basis:

- O(N^2): 
  - Bubble Sort, 
  - Selection Sort, 
  - Insertion Sort
- O(NlogN): 
  - Merge Sort
  - Quick Sort, 
  - Heap Sort, 
  - Binary Search Tree Sort, 
  - AVL Sort 
- O(N+k):
  -  Count Sort

#### 2.2 Some related problems:

##### Q1. For these different sorting algorithms, what are the time complexity and space complexity of these algorithms in different situation(average, best, worst)?  Can you provide a example of Best case and Worst case of each algorithms?

Ans:

##### Q2. Can you talk about how to implement a (***) sort algorithms?

Ans: 

##### Q3. What's a max heap or min heap?

Ans: Heap is tree, however for max heap each node is larger than all its children, for min heap, each node is smaller than all its children.

##### Q4. How to construct a heap?

Ans: generally speaking is two steps, but more details in code.

Step 1: insert the new element at the bottom 

Step 2: heapify the element from the bottom-up (swap if greater than parent, till root)

##### Q5. How to find the top K biggest number of a list?

Ans: 

Approach1: Sort all the list and take the top kth elements O(NlogN)

Approach2: For example use Selection Sort, get the biggest, second biggest, … until we get k elements. O(N*K)

Approach3: Use heap. Assume we only construct and update a heap with k elements, for each element we push it into the heap, so the time complexity is O(NlogK).

Approach4: Quick Select. Use the idea of pivot and Partition in Quick Sort. We know Partition can cut the list into 3 part, smaller than pivot and bigger than pivot and the pivot. For the part bigger than pivot, we compare the length of this part with K,  then decide to do the partition recursion in the left or in the right. Time Complexity is O(N).

##### Q6. How to merge n sorted lists to give one sorted list?

Ans: Divide and Conquer. Write a function to merge two sorter lists into one, then do the iteration to call the function. For example merge first and second linked list, we have a new linked list. Then merge this new one with third linked list.

##### Q7. When the scale of data is huge, simple implementation of quick sort may not work. For example in our project 1 we need to process traffic data which is huge and with many duplicated values, error "Max recursion depth exceeded" often raised. So how do you solve this problem？Can you talk about how to improve the quick sort algorithm?

Ans: One improvement is we can use random pivots. And the most efficient improvement is called 3 way quicksort. The change compared to original is that we cut the list into 3 parts, smaller than pivot, bigger than pivot and equal to pivot.

##### Q8. In quick sort algorithm, how to partition the list in place?

Ans: Details in code.

##### Q9. There are many algorithms in different area. But sometimes they have similarities. For example, quicksort is a sorting algorithm, while pre-order traverse algorithm is used in tree. Can you find the relationship of these two algorithms?

Ans: In pre-order, we first access the parent node, then call the sub pre-order function of its left children and right children. In quicksort, we use partition function to access the parent array, and cut it into two arrays: smaller than pivot and bigger than pivot,  then call the sub quicksort function of left array and right array. Thus, they are exactly the same.

##### Q10. Same to Q9, why merge sort is similar to post-order traverse algorithm?

Ans: In post-order, we first call the sub pre-order function of its left children and right children, then we access the parent node. In merge sort, we cut the array into two parts, we first call the sub function of these two part and do recursion, then we merge the result and return. Here two subarrays are two children node, the original array is the parent node. Thus, they are also the same.

