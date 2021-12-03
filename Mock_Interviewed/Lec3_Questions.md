# Mock Interview Questions

### 3. Tree

#### 3.1 basis:

- binary tree: 
  - Traverse Method DFS: pre-order, in-order, post-order [recursion / stack]
  - Traverse Method DFS: [queue]
- binary search tree(BST):
  - Once BST constructed, in-order walk => sort
- BST-> rotation->AVL
- RBT

#### 3.2 Some related problems:

##### Q1. What is binary search tree?

Ans: : left sub tree ≤ parent ≤ right sub tree for all nodes.

##### Q2. Given a list, how to construct the list into a BST?

Ans: For each value of list, insert it into the tree. Then how to insert a value into a BST tree? insert is a recursion function return head of a tree after insertion. if the value we want to insert is less than current node, we call recursion function for its left child, if the value is more than current node, we call recursion function for its right child. Only initialize a new node until current node is null.

##### Q3. How to search a node in BST/AVL?

Ans: Recursion.

##### Q4. How to delete a node from BST?

Ans: 

1)  Node to be deleted is the leaf: Simply remove from the tree. 
2)  Node to be deleted has only one child: Copy the child to the node and delete the child
3)  Node to be deleted has two children: Find inorder successor of the node.

##### Q5. What is a AVL Tree, how to measure a BST tree balanced or not?

Ans: Same to JiangFang's.

##### Q6. Given a list, how to construct the list into a AVL Tree?

Ans: The process is same to BST, for each value of list, insert it into the AVL tree.  But we need to add the rotation part into the original BST insertion function. After BST insertion, we can update the height of the ancestor node, and check whether it's balanced or not. If it's not balanced, check it belongs to which unbalanced case: left left, left right, right left, right right. Then do the corresponding rotation.

##### Q7. How to delete a node from AVL Tree?

Ans: 

1. Perform standard BST delete for w. 
2. Starting from w, traverse up and find the first unbalanced node. Let z be the first unbalanced node, y be the larger height child of z, and x be the larger height child of y. 
3.  Re-balance the tree by performing appropriate rotations on the subtree rooted with z according to 4 cases.
4.  After fixing z, we may have to fix ancestors of z as well. 

##### Q8. RBT

Ans:  Just say stories.

##### Q9. Time complexity of different operations between AVL Tree and Heap.

![image-20211128192046207](C:\Users\Lin Zeyin\AppData\Roaming\Typora\typora-user-images\image-20211128192046207.png)



