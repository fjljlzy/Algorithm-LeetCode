# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # DFS(post-order)
        # if not root:
        #     return 0
        # d1 = self.maxDepth(root.left)
        # d2 = self.maxDepth(root.right)
        # d = max(d1, d2) + 1
        # return d

        # DFS(post-order) 2
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # BFS (only stack)
        # if not root: return 0
        # q = [root]
        # depth = 0
        # while q:
        #     depth += 1
        #     nxt = []
        #     for node in q:
        #         if node.left:
        #             nxt.append(node.left)
        #         if node.right:
        #             nxt.append(node.right)
        #     q = nxt
        # return depth

        # BFS(deque) elegant!
        if not root: 
            return 0
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth
