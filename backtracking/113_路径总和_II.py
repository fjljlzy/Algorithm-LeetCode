# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
标准的回溯写法，注意nxt和最后的backtracking(None, ...)
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def backtracking(root, targetSum, path):
            if not root:
                if path and sum(path) == targetSum:
                    res.append(path[:])
                return
            path.append(root.val)
            nxt = []
            if root.left:
                nxt.append(root.left)
            if root.right:
                nxt.append(root.right)
            for node in nxt:
                backtracking(node, targetSum, path)
            if not nxt:
                backtracking(None, targetSum, path) 
            path.pop()

        backtracking(root, targetSum, [])
        return res
